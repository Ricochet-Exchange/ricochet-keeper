"""
Ricochet Distributor V2 Workflow

- Every 1 hour, for each exchange trigger:
    - Update oracle prices
    - Distribute

* Hard coded for just the USDC>>RIC v2 market right now

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.tellor_oracle_operator import TellorOracleOperator
from blocksec_plugin.ricochet_distributeV2_operator import RicochetDistributeOperator
from blocksec_plugin.ricochet_update_price_operator import RicochetUpdatePriceOperator
from constants.constants import PriceConstants

DISTRIBUTOR_WALLET_ADDRESS = Variable.get("distributor-v2-address")
V2_EXCHANGE_ADDRESSES = Variable.get("rexmarket-v2-addresses", deserialize_json=True)
SCHEDULE_INTERVAL = Variable.get("distribution-v2-schedule-interval", "0 * * * *")
GAS_MULTIPLIER = float(Variable.get("distribution-v2-gas-multiplier", 1.1))
USDCX_ADDRESS = "0xCAa7349CEA390F89641fe306D93591f87595dc1F"
RIC_ADDRESS = "0x263026E7e53DBFDce5ae55Ade22493f828922965"
MAX_GAS_PRICE = Variable.get("max-gas-price", PriceConstants.MAX_GAS_PRICE_DEFAULT)

default_args = {
    "owner": "ricochet",
    "depends_on_past": False,
    "start_date": datetime(2020, 1, 17),
    "email": ["mike@mikeghen.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


dag = DAG("ricochet_distribute_v2",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(DISTRIBUTOR_WALLET_ADDRESS)

done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

for exchange_address in V2_EXCHANGE_ADDRESSES:

    # Update input price
    update_input = RicochetUpdatePriceOperator(
        task_id="update_input_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        max_gas_price=MAX_GAS_PRICE,
        contract_address=exchange_address,
        token_address=USDCX_ADDRESS,
        nonce=current_nonce,
        dag=dag
    )
    current_nonce += 1

    # Update output price
    update_output = RicochetUpdatePriceOperator(
        task_id="update_output_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        max_gas_price=MAX_GAS_PRICE,
        contract_address=exchange_address,
        token_address=RIC_ADDRESS,
        nonce=current_nonce,
        dag=dag
    )
    current_nonce += 1


    distribute = RicochetDistributeOperator(
        task_id="distribute_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        max_gas_price=MAX_GAS_PRICE,
        contract_address=exchange_address,
        nonce=current_nonce,
        dag=dag
    )
    current_nonce += 1


    done << distribute << update_output << update_input
