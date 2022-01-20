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
from blocksec_plugin.rex_bank_update_collateral_price import RexBankUpdateCollateralPriceOperator
from blocksec_plugin.rex_bank_update_debt_price import RexBankUpdateDebtPriceOperator


REX_BANK_ADDRESSES = Variable.get("rex-bank-addresses")
SCHEDULE_INTERVAL = Variable.get("rex-bank-keeper-schedule-interval", "0 0 * * *")
REX_BANK_KEEPER_ADDRESS = Variable.get("rex-bank-keeper-address")

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

dag = DAG("rex_bank_keeper",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)

web3 = Web3Hook(web3_conn_id='infura').http_client
current_nonce = web3.eth.getTransactionCount(REX_BANK_KEEPER_ADDRESS)

done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

for bank_address in BANK_ADDRESSES:

    update_collateral_price = RexBankUpdateCollateralPriceOperator(
        task_id="update_collateral_price",
        web3_conn_id="infura",
        ethereum_wallet=REX_BANK_KEEPER_ADDRESS,
        gas_multiplier=1.1,
        gas=3000000,
        contract_address=bank_address,
        dag=dag
    )

    update_debt_price = RexBankUpdateDebtPriceOperator(
        task_id="update_debt_price",
        web3_conn_id="infura",
        ethereum_wallet=REX_BANK_KEEPER_ADDRESS,
        gas_multiplier=1.1,
        gas=3000000,
        contract_address=bank_address,
        dag=dag
    )

    done << update_debt_price << update_collateral_price
