"""

Example Swap Operation
- Swap RIC for MATIC

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.uniswap_swap_exact_tokens_for_tokens_operator import UniswapSwapExactTokensForTokensOperator
from blocksec_plugin.random_sleep_operator import RandomSleepOperator
from constants.constants import PriceConstants

SWAPPER_WALLET_ADDRESS = Variable.get("swapper-address")
SCHEDULE_INTERVAL = Variable.get("swap-schedule-interval", "0 * * * *")
SWAP_AMOUNT = Variable.get("ric-dca-swap-amount", 100000000) # 100 USDC
MAX_GAS_PRICE = Variable.get("max-gas-price", PriceConstants.MAX_GAS_PRICE_DEFAULT)

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


dag = DAG("ricochet_dca",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(SWAPPER_WALLET_ADDRESS)

done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

stall = RandomSleepOperator(
    task_id="stall",
    min=60*3,
    max=60*15,
    dag=dag
)

swap = UniswapSwapExactTokensForTokensOperator(
    task_id="swap",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.2,
    gas=3000000,
    max_gas_price=MAX_GAS_PRICE,
    contract_address="0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506",
    amount_in=SWAP_AMOUNT,
    amount_out_min=0,
    to=SWAPPER_WALLET_ADDRESS,
    path=["0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174","0x263026E7e53DBFDce5ae55Ade22493f828922965"],
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

done << confirm_swap << swap << stall
