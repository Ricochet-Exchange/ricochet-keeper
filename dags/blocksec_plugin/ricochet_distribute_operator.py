from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

DISTRIBUTE_ABI = '''[{
      "inputs": [],
      "name": "distribute",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }]'''

class RicochetDistributeOperator(ContractInteractionOperator):
    """
    Calls `distribute` on Ricochet contracts
    """
    template_fields = []

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
        super().__init__(web3_conn_id,
                        ethereum_wallet,
                        contract_address,
                        gas_key,
                        gas_multiplier,
                        gas,
                        nonce,
                        *args,
                        **kwargs)
        self.abi_json = DISTRIBUTE_ABI

    def execute(self, context):
        # Create the contract factory
        print("Processing distribution for Ricochet at {0} by EOA {1}".format(
            self.contract_address, self.wallet.public_address
        ))

        transaction_hash = super().transact(self.contract_address, self.abi_json, 'distribute')

        # contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        # # Form the signed transaction
        # withdraw_txn = contract.functions.distribute()\
        #                                  .buildTransaction(dict(
        #                                    nonce=int(self.nonce),
        #                                    gasPrice = int(self.web3.eth.gasPrice *\
        #                                               self.gas_multiplier),
        #                                    gas = self.gas
        #                                   ))
        # signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # # Send the transaction
        # transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("Sent distribute... transaction hash: {0}".format(transaction_hash.hex()))
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
