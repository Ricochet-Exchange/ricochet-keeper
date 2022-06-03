"""
Ricochet Stream Watch
- Checks all the streamers and closes streams that are close to running out
"""
from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.api.client.local_client import Client
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.ricochet_streamer_list_operator import RicochetStreamerListOperator
from blocksec_plugin.abis import REX_ABI, ERC20_ABI
from datetime import datetime, timedelta
from constants.constants import ScheduleConstants, Utils
import requests


CLOSER_WALLET_ADDRESS = Variable.get("closer-address")
EXCHANGE_ADDRESSES = Variable.get("ricochet-exchange-addresses", deserialize_json=True)
SCHEDULE_INTERVAL = Variable.get("watch-schedule-interval", ScheduleConstants.RICOCHET_STREAM_WATCH)
SUPERFLUID_GRAPHQL_POLYGON_URI = Variable.get("superfluid-graphql-polygon-uri", default_var="https://api.thegraph.com/subgraphs/name/superfluid-finance/protocol-v1-matic")

default_args = Utils.get_DAG_args()


dag = DAG("ricochet_stream_watch",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)


done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)


def review_streamers_and_trigger_closures(**context):
    """
    Trigger payouts for miners
    """
    execution_date = context['execution_date'].isoformat()
    exchange_address = context['exchange_address']

    query = '{' +'account(id: "{}")'.format(exchange_address) + ''' {
            inflows {
                id
            }
        }
    }
    '''

    request = requests.post(SUPERFLUID_GRAPHQL_POLYGON_URI, json={'query': query})
    response = request.json()
    streamers = [streamer['id'].split("-")[0] for streamer in response['data']['account']['inflows']]
    print("Streamers", streamers)

    web3 = Web3Hook(web3_conn_id='infura').http_client
    c = Client(None, None)
    index = 0
    current_nonce = web3.eth.getTransactionCount(CLOSER_WALLET_ADDRESS)
    for streamer in streamers:

        # Check if the streamers balance is less that 8 hours of streamer
        ricochet = web3.eth.contract(address=exchange_address, abi=REX_ABI)
        input_token = ricochet.functions.getInputToken().call()
        input_token = web3.eth.contract(address=input_token, abi=ERC20_ABI)
        balance = input_token.functions.balanceOf(streamer).call()
        rate = ricochet.functions.getStreamRate(streamer).call()
        is_closable = balance < rate * 60 * 60 * 8 # balance is greater than 8 hours of streaming
        print(f"Checked {streamer}, balance: {balance}, rate: {rate}, is_closable: {is_closable}")
        # Trigger ricochet_stream_closer is the stream is closable
        if is_closable:
            try:
                conf = {
                    "streamer_address": Web3.toChecksumAddress(streamer),
                    "exchange_address": Web3.toChecksumAddress(exchange_address),
                    "nonce": current_nonce + index
                }
            except ValueError:
                print("Fail", miner_payout)
                continue

            index += 1
            result = c.trigger_dag(dag_id='ricochet_stream_closure',
                          run_id=streamer + execution_date,
                          conf=conf)
            print("Trigged closure: ", result, conf)
    return index # number of channels closed


for exchange_address in EXCHANGE_ADDRESSES:

    closures = PythonOperator(
        task_id='closures_' + exchange_address,
        provide_context=True,
        python_callable=review_streamers_and_trigger_closures,
        op_kwargs={'exchange_address': exchange_address},
        dag=dag
    )


    done << closures
