from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook
import requests,json
from time import sleep

ERC20_ABI = '''
[{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
'''

class ERC20BalanceOfOperator(BaseOperator):
    template_fields = []
    ui_color = "#BC9EC1"

    @apply_defaults
    def __init__(self,
                 contract_address,
                 account,
                 web3_conn_id='web3_default',
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.account = account
        self.web3_conn_id = web3_conn_id
        self.contract_address = contract_address
        self.web3 = Web3Hook(web3_conn_id=self.web3_conn_id).http_client

    def execute(self, context):
        # Create the contract factory
        print("Processing approve of {0} by EOA {1}".format(
            self.contract_address, self.wallet.public_address
        ))
        contract = self.web3.eth.contract(self.contract_address, abi=ERC20_ABI)
        return contract.functions.balanceOf(self.account).call()
