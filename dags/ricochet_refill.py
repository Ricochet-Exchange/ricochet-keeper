"""

Refills keeper addresses with MATIC
- Desposit RIC into the REX Bank
- Borrow USDCx and Downgrade
- Swap USDC to MATIC

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from blocksec_plugin.ethereum_transaction_confirmation_sensor import EthereumTransactionConfirmationSensor
from blocksec_plugin.erc20_approve_operator import ERC20ApprovalOperator
from blocksec_plugin.uniswap_swap_exact_tokens_for_eth_operator import UniswapSwapExactTokensForETHOperator
from blocksec_plugin.supertoken_downgrade_operator import SuperTokenDowngradeOperator
from blocksec_plugin.rex_bank_borrow import RexBankBorrowOperator
from blocksec_plugin.rex_bank_deposit import RexBankDepositOperator
from blocksec_plugin.erc20_balanceof_operator import ERC20BalanceOfOperator
from constants.constants import AddressConstants, PriceConstants, ScheduleConstants, Utils

REX_BANK_ADDRESS = Variable.get("rex-bank-address")
SWAPPER_WALLET_ADDRESS = Variable.get("distributor-address")
SCHEDULE_INTERVAL = Variable.get("refill-schedule-interval", ScheduleConstants.RICOCHET_REFILL)
ROUTER_ADDRESS = Variable.get("router-address", AddressConstants.SUSHI_V2_ROUTER_02) # SushiSwap
RIC_TOKEN_ADDRESS = Variable.get("ric-token-address", AddressConstants.RIC_TOKEN)
USDCX_TOKEN_ADDRESS = Variable.get("usdcx-token-address", AddressConstants.USDCx_TOKEN)
USDC_TOKEN_ADDRESS = Variable.get("usdc-token-address", AddressConstants.USDC_TOKEN)
MATIC_TOKEN_ADDRESS = Variable.get("matic-token-address", AddressConstants.WMATIC_TOKEN)
MAX_GAS_PRICE = Variable.get("max-gas-price", PriceConstants.MAX_GAS_PRICE_DEFAULT)

default_args = Utils.get_DAG_args()

dag = DAG("ricochet_refill",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(SWAPPER_WALLET_ADDRESS)

# approve_vault_deposit >> vault_deposit >> vault_borrow >> downgrade >> approve_swap >> swap


done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

balance = ERC20BalanceOfOperator(
    task_id="balance",
    web3_conn_id="infura",
    contract_address=RIC_TOKEN_ADDRESS,
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    account=SWAPPER_WALLET_ADDRESS,
    dag=dag
)

approve_deposit = ERC20ApprovalOperator(
    task_id="approve_deposit",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_DEFAULT,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=RIC_TOKEN_ADDRESS,
    spender=REX_BANK_ADDRESS,
    amount="{{task_instance.xcom_pull(task_ids='balance')}}",
    dag=dag
)

confirm_approve_deposit = EthereumTransactionConfirmationSensor(
    task_id="confirm_approve_deposit",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='approve_deposit')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)

deposit = RexBankDepositOperator(
    task_id="deposit",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_DEFAULT,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=REX_BANK_ADDRESS,
    amount="{{task_instance.xcom_pull(task_ids='balance')}}",
    dag=dag
)

confirm_deposit = EthereumTransactionConfirmationSensor(
    task_id="confirm_deposit",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='deposit')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)

borrow = RexBankBorrowOperator(
    task_id="borrow",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_DEFAULT,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=REX_BANK_ADDRESS,
    amount=-1, # max borrow
    dag=dag
)

confirm_borrow = EthereumTransactionConfirmationSensor(
    task_id="confirm_borrow",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='borrow')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)


downgrade = SuperTokenDowngradeOperator(
    task_id="downgrade",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_DEFAULT,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=USDCX_TOKEN_ADDRESS,
    amount=-1, # 0.6 USDCx
    dag=dag
)

confirm_downgrade = EthereumTransactionConfirmationSensor(
    task_id="confirm_downgrade",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='downgrade')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)

approve_swap = ERC20ApprovalOperator(
    task_id="approve_swap",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_DEFAULT,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=USDC_TOKEN_ADDRESS,
    spender=ROUTER_ADDRESS,
    amount=-1, # 1 RIC
    dag=dag
)

confirm_approve_swap = EthereumTransactionConfirmationSensor(
    task_id="confirm_approve_swap",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='approve_swap')}}",
    confirmations=1,
    poke_interval=5,
    timeout=60 * 20,
    dag=dag
)


swap = UniswapSwapExactTokensForETHOperator(
    task_id="swap",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=PriceConstants.GAS_MULTIPLIER_SWAP,
    gas=PriceConstants.GAS_DEFAULT,
    max_gas_price=MAX_GAS_PRICE,
    contract_address=ROUTER_ADDRESS,
    amount_in=-1,
    amount_out_min=0,
    to=SWAPPER_WALLET_ADDRESS,
    path=[USDC_TOKEN_ADDRESS, MATIC_TOKEN_ADDRESS],
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

balance >> approve_deposit >> confirm_approve_deposit >>\
deposit >> confirm_deposit >>\
borrow >> confirm_borrow >>\
downgrade >> confirm_downgrade >>\
approve_swap >> confirm_approve_swap >>\
swap >> confirm_swap >>\
done
