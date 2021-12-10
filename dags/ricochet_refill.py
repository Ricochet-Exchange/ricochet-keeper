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
from blocksec_plugin.abis import TELLOR_ABI
from json import loads
import requests

REX_BANK_ADDRESS = "0x91093c77720e744F415D33551C2fC3FAf7333c8c"
RIC_TOKEN_ADDRESS = "0x263026E7e53DBFDce5ae55Ade22493f828922965"
USDCX_TOKEN_ADDRESS = "0xCAa7349CEA390F89641fe306D93591f87595dc1F"
USDC_TOKEN_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
MATIC_TOKEN_ADDRESS = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"
ROUTER_ADDRESS = "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"
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

# approve_vault_deposit >> vault_deposit >> vault_borrow >> downgrade >> approve_swap >> swap


done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

approve_deposit = ERC20ApprovalOperator(
    task_id="approve_deposit",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.1,
    gas=3000000,
    contract_address=RIC_TOKEN_ADDRESS,
    spender=REX_BANK_ADDRESS,
    amount=1000000000000000000, # 1 RIC
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
    gas_multiplier=1.1,
    gas=3000000,
    contract_address=REX_BANK_ADDRESS,
    amount=1000000000000000000, # 1 RIC
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
    task_id="deposit",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.1,
    gas=3000000,
    contract_address=REX_BANK_ADDRESS,
    amount=600000000000000000, # 0.6 USDCx
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
    task_id="deposit",
    web3_conn_id="infura",
    ethereum_wallet=SWAPPER_WALLET_ADDRESS,
    gas_multiplier=1.1,
    gas=3000000,
    contract_address=USDCX_CONTRACT_ADDRESS,
    amount=600000000000000000, # 0.6 USDCx
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
    gas_multiplier=1.1,
    gas=3000000,
    contract_address=USDC_TOKEN_ADDRESS,
    spender=REX_BANK_ADDRESS,
    amount=600000, # 1 RIC
    dag=dag
)

confirm_approve_swap = EthereumTransactionConfirmationSensor(
    task_id="confirm_approve_swap",
    web3_conn_id="infura",
    transaction_hash="{{task_instance.xcom_pull(task_ids='confirm_approve_swap')}}",
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
    router_address=ROUTER_ADDRESS,
    amount_in=600000,
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

approve_deposit >> confirm_approve_deposit >>\
deposit >> confirm_deposit >>\
borrow >> confirm_borrow >>\
downgrade >> confirm_downgrade >>\
approve_swap >> confirm_approve_swap >>\
swap >> confirm_swap >>\
done
