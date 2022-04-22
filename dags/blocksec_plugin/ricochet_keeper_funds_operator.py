from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests, json
from blocksec_plugin.web3_hook import Web3Hook

class KeeperFundsReporterOperator(BaseOperator):
    """
    Check MATIC on each keeper and report to discord if lower than threshold
    """
    template_fields = []
    ui_color = "#C7D59F"

    @apply_defaults
    def __init__(self,
                 discord_webhook,
                 keepers,
                 threshold,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.discord_webhook = discord_webhook
        self.threshold = threshold
        self.keepers = keepers


    def execute(self, context):
        """
        Check the matic of the each keeper and report to discord
        """
        low_balance_keepers = []
        web3 = Web3Hook(web3_conn_id='infura').http_client

        print(f"Checking for keepers - {self.keepers.values()}")

        for username, address in self.keepers.items():
            balance = web3.eth.get_balance(address)
            if balance < self.threshold:
                low_balance_keepers.append(f"@{username}: {address}")
        
        if len(low_balance_keepers) > 0:
            message = f"The following keepers have balance lower then {self.threshold}: " + ", ".join(low_balance_keepers)
            request = requests.post(self.discord_webhook, json={"content": message})
            print(request.status_code, request.text)

        return
