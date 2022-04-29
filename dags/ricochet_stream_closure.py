"""
Ricochet Stream Closure

- This DAG is triggered by

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.ricochet_streamer_close_operator import RicochetStreamerCloseOperator
from blocksec_plugin.abis import REX_ABI
from constants.constants import PriceConstants, ScheduleConstants, Utils

CLOSER_WALLET_ADDRESS = Variable.get("closer-address")
SCHEDULE_INTERVAL = Variable.get("close-schedule-interval", ScheduleConstants.RICOCHET_STREAM_CLOSURE)
MAX_GAS_PRICE = Variable.get("max-gas-price", PriceConstants.MAX_GAS_PRICE_DEFAULT)

default_args = Utils.get_DAG_args(retries=3, retry_delay=timedelta(minutes=5))


dag = DAG("ricochet_stream_closure",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)


done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

close_stream = RicochetStreamerCloseOperator(
    task_id="close_stream",
    web3_conn_id="infura",    # Set in Aiflow Connections UI
    ethereum_wallet=CLOSER_WALLET_ADDRESS, # Set in Airflow Connections UI
    streamer_address='{{ dag_run.conf["streamer_address"] }}',
    contract_address='{{ dag_run.conf["exchange_address"] }}',
    nonce='{{ dag_run.conf["nonce"] }}',
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_STREAM_CLOSURE,
    max_gas_price=MAX_GAS_PRICE,
    dag=dag,
)

confirm_close = EthereumTransactionConfirmationSensor(
    task_id="confirm_send",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='close_stream')}}",
    confirmations=1,
    poke_interval=20,
    timeout=60 * 3,
    dag=dag
)


done << confirm_close << close_stream
