"""
Check keeper funds and report to discord

- This DAG is should be triggered once a day.

"""
from airflow import DAG
from airflow.models import Variable
from datetime import datetime, timedelta
from blocksec_plugin.web3_hook import Web3Hook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from constants.constants import PriceConstants
from blocksec_plugin.ricochet_keeper_funds_operator import KeeperFundsReporterOperator

# eg - {"@shreyaspapi": "0x6e509201e340cd24c35f235802ee1de044b0f16f"}
KEEPER_ADDRESSES = Variable.get("keeper-addresses", deserialize_json=True)
SCHEDULE_INTERVAL = Variable.get("keeper-funds-dag-interval", "15 * * * *")
DISCORD_WEBHOOK = Variable.get("discord-webhook-keeper-funds")

default_args = {
    "owner": "ricochet",
    "depends_on_past": False,
    "start_date": datetime(2020, 3, 29),
    "email": ["mike@mikeghen.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}


dag = DAG("ricochet_keeper_funds",
          max_active_runs=1,
          catchup=False,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL)


done = BashOperator(
    task_id='done',
    bash_command='date',
    dag=dag,
)

keeper_reporter = KeeperFundsReporterOperator(
    task_id='keeper_reporter',
    discord_webhook=DISCORD_WEBHOOK,
    keepers=KEEPER_ADDRESSES,
    threshold=PriceConstants.KEEPER_FUNDS_THRESHOLD,
    dag=dag
)


done << keeper_reporter
