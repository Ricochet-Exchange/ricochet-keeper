"""

Example Swap Operation
- Swap RIC for MATIC
- Note - Make sure to give unlimited approval to 0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506.
"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.uniswap_swap_exact_tokens_for_tokens_operator import UniswapSwapExactTokensForTokensOperator
from blocksec_plugin.random_sleep_operator import RandomSleepOperator
from constants.constants import AddressConstants, PriceConstants, ScheduleConstants, Utils

SWAPPER_WALLET_ADDRESS = Variable.get("swapper-address")
SCHEDULE_INTERVAL = Variable.get("swap-schedule-interval", ScheduleConstants.RICOCHET_DCA)
SWAP_AMOUNT = Variable.get("ric-dca-swap-amount", PriceConstants.RIC_DCA_SWAP_AMOUNT) # 100 USDC
MAX_GAS_PRICE = Variable.get("max-gas-price", PriceConstants.MAX_GAS_PRICE_DEFAULT)

default_args = Utils.get_DAG_args()


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
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_SWAP,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=AddressConstants.SUSHI_V2_ROUTER_02,
    amount_in=SWAP_AMOUNT,
    amount_out_min=0,
    to=SWAPPER_WALLET_ADDRESS,
    path=[AddressConstants.USDC_TOKEN, AddressConstants.RIC_TOKEN],
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
