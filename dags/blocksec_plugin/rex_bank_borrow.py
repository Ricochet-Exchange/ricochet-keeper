from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook

BORROW_ABI = '''[{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"vaultBorrow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'''

class RexBankBorrowOperator(BaseOperator):

    template_fields = []

    @apply_defaults
    def __init__(self,
                 amount,
                 web3_conn_id='web3_default',
                 ethereum_wallet='default_wallet',
                 contract_address=None,
                 gas_key="fast",
                 gas_multiplier=1,
                 gas=1200000,
                 nonce=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.web3_conn_id = web3_conn_id
        self.ethereum_wallet = ethereum_wallet
        self.contract_address = contract_address
        self.abi_json = BORROW_ABI
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
        contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        # Form the signed transaction
        deposit = contract.functions.vaultBorrow(self.amount)\
                                         .buildTransaction(dict(
                                           nonce=int(self.nonce),
                                           gasPrice = int(self.web3.eth.gasPrice *\
                                                      self.gas_multiplier),
                                           gas = self.gas
                                          ))
        signed_txn = self.web3.eth.account.signTransaction(deposit, self.wallet.private_key)
        # Send the transaction
        transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("Sent vaultBorrow({1})... transaction hash: {0}".format(self.amount, transaction_hash.hex()))
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
