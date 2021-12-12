from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

APPROVE_ABI = '''[{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'''

class ERC20ApprovalOperator(ContractInteractionOperator):
    """
    Calls `distribute` on Ricochet contracts
    """
    template_fields = []

    @apply_defaults
    def __init__(self,
                 web3_conn_id='web3_default',
                 ethereum_wallet='default_wallet',
                 contract_address=None,
                 spender=None,
                 amount=None,
                 gas_key="fast",
                 gas_multiplier=1,
                 gas=1200000,
                 nonce=None,
                 *args,
                 **kwargs):
        super().__init__(web3_conn_id, 
                        ethereum_wallet,
                        contract_address,
                        spender,
                        amount,
                        gas_key,
                        gas_multiplier,
                        gas,
                        nonce,
                        *args,
                        **kwargs)
        self.abi_json = APPROVE_ABI

    def execute(self, context):
        # Create the contract factory
        print("Processing approve of {0} by EOA {1}".format(
            self.contract_address, self.wallet.public_address
        ))

        transaction_hash = super().transact(self.contract_address, self.abi_json, 'approve', self.spender, self.amount)

        # contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        # # Form the signed transaction
        # withdraw_txn = contract.functions.approve(self.spender, self.amount)\
        #                                  .buildTransaction(dict(
        #                                    nonce=int(self.nonce),
        #                                    gasPrice = int(self.web3.eth.gasPrice *\
        #                                               self.gas_multiplier),
        #                                    gas = self.gas
        #                                   ))
        # signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # # Send the transaction
        # transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Sent approve({self.spender}, {self.amount}) txn hash: {transaction_hash.hex()}")
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
