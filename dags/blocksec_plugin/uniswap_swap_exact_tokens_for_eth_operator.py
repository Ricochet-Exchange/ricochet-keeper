from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook
import requests,json
from time import time

SWAP_ABI = '''[{
    "inputs":[
        {"internalType":"uint256","name":"amountIn","type":"uint256"},
        {"internalType":"uint256","name":"amountOutMin","type":"uint256"},
        {"internalType":"address[]","name":"path","type":"address[]"},
        {"internalType":"address","name":"to","type":"address"},
        {"internalType":"uint256","name":"deadline","type":"uint256"}
    ],
    "name":"swapExactTokensForETH",
    "outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],
    "stateMutability":"nonpayable","type":"function"
}]'''
ERC20_ABI = '''
[{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
'''

class UniswapSwapExactTokensForETHOperator(BaseOperator):
    """
    Calls `swapExactTokensForETH` on a Uniswap Router contract
    * Assumes amount of tokens has been approved already
    """
    template_fields = []
    ui_color = "#EBBAB9"

    @apply_defaults
    def __init__(self,
                 web3_conn_id='web3_default',
                 ethereum_wallet='default_wallet',
                 router_address=None,
                 amount_in=0,
                 amount_out_min=0,
                 path=[],
                 to=None,
                 deadline=None,
                 gas_key="fast",
                 gas_multiplier=1,
                 gas=1200000,
                 nonce=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.router_address = router_address
        self.amount_in = amount_in
        self.amount_out_min = amount_out_min
        self.path = path
        self.to = to
        if not deadline:
            self.deadline = time() + 300
        else:
            self.deadline = dealine
        self.web3_conn_id = web3_conn_id
        self.ethereum_wallet = ethereum_wallet
        self.contract_address = router_address
        self.abi_json = SWAP_ABI
        self.gas_key = gas_key
        self.gas_multiplier = gas_multiplier
        self.gas = gas
        self.web3 = Web3Hook(web3_conn_id=self.web3_conn_id).http_client
        self.wallet = EthereumWalletHook(ethereum_wallet=self.ethereum_wallet)
        if nonce:
            self.nonce = nonce
        else: # Look up the last nonce for this wallet
            self.nonce = self.web3.eth.getTransactionCount(self.wallet.public_address)

    def execute(self, context):
        # Create the contract factory
        print("Processing distribution for Ricochet at {0} by EOA {1}".format(
            self.contract_address, self.wallet.public_address
        ))
        contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        if self.amount < 0:
            # Max swap
            input_token = self.web3.eth.contract(self.path[0], abi=ERC20_ABI)
            self.amount = input_token.functions.balanceOf(self.wallet.public_address).call()

        # Form the signed transaction
        withdraw_txn = contract.functions.swapExactTokensForETH(self.amount_in,
                                                                self.amount_out_min,
                                                                self.path,
                                                                self.to,
                                                                int(self.deadline))\
                                         .buildTransaction(dict(
                                           nonce=int(self.nonce),
                                           gasPrice = int(self.web3.eth.gasPrice *\
                                                      self.gas_multiplier),
                                           gas = self.gas
                                          ))
        signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # Send the transaction
        transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Sent swapExactTokensForETH({self.amount_in},{self.amount_out_min},{self.path},{self.to},{self.deadline})... transaction hash: {transaction_hash.hex()}")
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
