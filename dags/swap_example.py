"""

Example Swap Operation
- Swap RIC for MATIC

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.tellor_oracle_operator import TellorOracleOperator
from blocksec_plugin.erc20_approve_operator import ERC20ApprovalOperator
from blocksec_plugin.uniswap_swap_exact_tokens_for_eth_operator import UniswapSwapExactTokensForETHOperator
from blocksec_plugin.abis import TELLOR_ABI
from json import loads
import requests

SWAPPER_WALLET_ADDRESS = Variable.get("distributor-address")

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


dag = DAG("swap_example",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval="0 * * * *")

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(SWAPPER_WALLET_ADDRESS)

done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

approve = ERC20ApprovalOperator(
    task_id="approve",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.2,
    gas=3000000,
    contract_address="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
    spender="0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506",
    amount=1000000,
    dag=dag
)

confirm_approve = EthereumTransactionConfirmationSensor(
    task_id="confirm_approve",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='approve')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)

swap = UniswapSwapExactTokensForETHOperator(
    task_id="swap",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.2,
    gas=3000000,
    router_address="0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506",
    amount_in=1000000,
    amount_out_min=0,
    to=SWAPPER_WALLET_ADDRESS,
    path=["0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174","0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"],
    dag=dag
)

confirm_swap = EthereumTransactionConfirmationSensor(
    task_id="confirm_swap",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='swap')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)

done << confirm_swap << swap << confirm_approve << approve
