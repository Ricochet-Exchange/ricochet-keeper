from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook
from web3.exceptions import InvalidAddress
from constants.constants import PriceConstants

class ContractInteractionOperator(BaseOperator):
    """
    Executes a generalized contract interaction
    """

    template_fields = ['contract_address', 'function', 'args', 'abi_json']

    @apply_defaults
    def __init__(self,
                 contract_address,
                 abi_json,
                 function=None,
                 function_args=None,
                 web3_conn_id='web3_default',
                 ethereum_wallet='default_wallet',
                 gas_key="fast",
                 gas_multiplier=1,
                 gas=1200000,
                 max_gas_price=PriceConstants.MAX_GAS_PRICE_DEFAULT, # not implemented
                 nonce=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.web3_conn_id = web3_conn_id
        self.ethereum_wallet = ethereum_wallet
        self.contract_address = contract_address
        self.function = function
        self.function_args = function_args
        self.gas_key = gas_key
        self.gas_multiplier = gas_multiplier
        self.gas = gas
        self.max_gas_price = max_gas_price
        self.web3 = Web3Hook(web3_conn_id=self.web3_conn_id).http_client
        self.wallet = EthereumWalletHook(ethereum_wallet=self.ethereum_wallet)
        try: # check if this is set, otherwise set it with
            self.abi_json
        except AttributeError:
            self.abi_json = abi_json
        if nonce:
            self.nonce = nonce
        else: # Look up the last nonce for this wallet
            self.nonce = self.web3.eth.getTransactionCount(self.wallet.public_address)

        self.contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)

    def confirm_success(self, txn):
        try:
            self.function(**self.function_args).estimateGas(transaction=txn)
            return True
        except ValueError:
            return False

    def execute(self, context):
        if not self.contract:
            self.contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)

        print(f"Executing {self.function} with args {self.function_args} on {self.contract_address}")
        raw_txn = self.function(**self.function_args)\
                             .buildTransaction(dict(
                               nonce=int(self.nonce),
                               maxFeePerGas=int(int(float(self.web3.eth.gas_price) * float(self.gas_multiplier)) + float(self.web3.eth.max_priority_fee)),
                               maxPriorityFeePerGas=self.web3.eth.max_priority_fee,
                               gas = self.gas
                              ))
        # if not self.confirm_success(raw_txn):
        #     raise ValueError("Transaction failed to confirm")
        signed_txn = self.web3.eth.account.signTransaction(raw_txn, self.wallet.private_key)
        transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Txn hash: {transaction_hash.hex()}")
        return str(transaction_hash.hex())
