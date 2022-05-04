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


DISTRIBUTOR_WALLET_ADDRESS = Variable.get("distributor-v2-address")
"""
V2_EXCHANGE_ADDRESSES example:
{
    exchange_address: [tokenA_address, tokenB_address],
    "0x58Db2937B08713214014d2a579C3088db826Fad1": ["0xCAa7349CEA390F89641fe306D93591f87595dc1F","0x263026E7e53DBFDce5ae55Ade22493f828922965"],
    "0xF6a03FCf12Cdc8066aFaf12255105CA301E15ba6": ["0xCAa7349CEA390F89641fe306D93591f87595dc1F","0x27e1e4E6BC79D93032abef01025811B7E4727e85"]
}
"""
V2_EXCHANGE_ADDRESSES = Variable.get("rexmarket-v2-addresses", deserialize_json=True)
SCHEDULE_INTERVAL = Variable.get("distribution-v2-schedule-interval", "0 * * * *")
GAS_MULTIPLIER = float(Variable.get("distribution-v2-gas-multiplier", 1.1))
USDCX_ADDRESS = "0xCAa7349CEA390F89641fe306D93591f87595dc1F"
RIC_ADDRESS = "0x263026E7e53DBFDce5ae55Ade22493f828922965"

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

for exchange_address, tokens in V2_EXCHANGE_ADDRESSES.items():

    # Update input price
    update_a = RicochetUpdatePriceOperator(
        task_id="update_a_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        contract_address=exchange_address,
        token_address=tokens[0],
        nonce=current_nonce,
        dag=dag
    )

    update_b = RicochetUpdatePriceOperator(
        task_id="update_b_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        contract_address=exchange_address,
        token_address=tokens[1],
        nonce=current_nonce + len(V2_EXCHANGE_ADDRESSES),
        dag=dag
    )

    distribute = RicochetDistributeOperator(
        task_id="distribute_" + exchange_address,
        web3_conn_id="infura",
        ethereum_wallet=DISTRIBUTOR_WALLET_ADDRESS,
        gas_multiplier=GAS_MULTIPLIER,
        gas=3000000,
        contract_address=exchange_address,
        nonce=current_nonce + 2 * len(V2_EXCHANGE_ADDRESSES),
        dag=dag
    )
    current_nonce += 1


    done << distribute << update_a << update_b
