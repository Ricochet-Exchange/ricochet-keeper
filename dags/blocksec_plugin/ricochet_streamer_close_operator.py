from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import RICOCHET_ABI


class RicochetStreamerCloseOperator(ContractInteractionOperator):
    """
    Closes a streamers stream using `closeStream`
    """
    template_fields = ['streamer_address', 'exchange_address', 'nonce']

    @apply_defaults
    def __init__(self,
                 web3_conn_id='web3_default',
                 ethereum_wallet=None,
                 streamer_address=None,
                 exchange_address=None,
                 gas=1200000,
                 gas_multiplier=1,
                 nonce=None,
                 *args,
                 **kwargs):
        super().__init__(web3_conn_id,
                        ethereum_wallet,
                        streamer_address,
                        exchange_address,
                        gas,
                        gas_multiplier,
                        nonce,
                        *args,
                        **kwargs)


    def execute(self, context):
        # Create the contract factory
        print("Processing closeStream for Ricochet at {0} for {1} by {2}".format(
            self.exchange_address, self.streamer_address, self.wallet.public_address
        ))
        
        transaction_hash = super().transact(self.exchange_address, RICOCHET_ABI, 'closeStream', self.streamer_address)

        # contract = self.web3.eth.contract(self.exchange_address, abi=RICOCHET_ABI)
        # # Form the signed transaction
        # withdraw_txn = contract.functions.closeStream(self.streamer_address)\
        #                                  .buildTransaction(dict(
        #                                    nonce=int(self.nonce),
        #                                    gasPrice = self.web3.eth.gasPrice * self.gas_multiplier,
        #                                    gas = self.gas
        #                                   ))
        # signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # # Send the transaction
        # transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("Sent closeStream()... transaction hash: {0}".format(transaction_hash.hex()))
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
