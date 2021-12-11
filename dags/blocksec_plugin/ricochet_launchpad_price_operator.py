from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook

SHARE_PRICE_ABI = '''[{"inputs":[],"name":"getSharePrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'''

class RicochetLaunchpadPrice(BaseOperator):
    """
    Checks the price of a Ricochet Launchpad
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 web3_conn_id='web3_default',
                 contract_address=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.web3_conn_id = web3_conn_id
        self.contract_address = contract_address
        self.web3 = Web3Hook(web3_conn_id=self.web3_conn_id).http_client
        
    def execute(self, context):
        contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        share_price = contract.functions.getSharePrice().call()
        return share_price
