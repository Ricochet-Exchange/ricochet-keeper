from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook
import requests,json
from time import sleep

DISTRIBUTE_ABI = '''[{"inputs":[],"name":"harvest","outputs":[],"stateMutability":"nonpayable","type":"function"}]'''

class RicochetHarvestOperator(BaseOperator):
    """
    Calls `harvest` on Ricochet contracts
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
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
        self.abi_json = DISTRIBUTE_ABI
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
        # Form the signed transaction
        withdraw_txn = contract.functions.harvest()\
                                         .buildTransaction(dict(
                                           nonce=int(self.nonce),
                                           gasPrice = int(min(30,self.web3.eth.gasPrice) *\
                                                      self.gas_multiplier),
                                           gas = self.gas
                                          ))
        signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # Send the transaction
        transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("Sent distribute... transaction hash: {0}".format(transaction_hash.hex()))
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
