"""
Ricochet Distributor Workflow

- Every 1 hour, for each exchange trigger `distribute()`

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.tellor_oracle_operator import TellorOracleOperator
from blocksec_plugin.ricochet_harvest_operator import RicochetHarvestOperator
from blocksec_plugin.abis import TELLOR_ABI
from json import loads
import requests

HARVESTER_WALLET_ADDRESS = Variable.get("harvester-address")
EXCHANGE_ADDRESSES = Variable.get("ricochet-lp-addresses", deserialize_json=True)
SCHEDULE_INTERVAL = Variable.get("harvester-schedule-interval", "0 * * * *")
GAS_MULTIPLIER = Variable.get("harvester-gas-multiplier", 1.2)

default_args = {
    "owner": "ricochet",
    "depends_on_past": False,
    "start_date": datetime(2020, 3, 29),
    "email": ["mike@mikeghen.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1)
}


dag = DAG("ricochet_harvest",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(HARVESTER_WALLET_ADDRESS)

done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

for nonce_offset, exchange_address in enumerate(EXCHANGE_ADDRESSES):
    distribute = RicochetHarvestOperator(
        task_id="harvest_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=HARVESTER_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        contract_address=exchange_address,
        nonce=current_nonce + nonce_offset,
        dag=dag
    )

    confirm_distribute = EthereumTransactionConfirmationSensor(
        task_id="confirm_harvest_" + exchange_address,
        web3_conn_id="infura",
        transaction_hash="{{task_instance.xcom_pull(task_ids='harvest_" + exchange_address + "')}}",
        confirmations=1,
        poke_interval=5,
        timeout=60 * 20,
        dag=dag
    )

    done << confirm_distribute << distribute
