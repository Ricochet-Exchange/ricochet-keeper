from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
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

class UniswapSwapExactTokensForETHOperator(ContractInteractionOperator):
    """
    Calls `swapExactTokensForETH` on a Uniswap Router contract
    * Assumes amount of tokens has been approved already
    """
    template_fields = []

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
                 gas_key="fast", #
                 gas_multiplier=1, #
                 gas=1200000, #
                 nonce=None, #
                 *args, #
                 **kwargs): #
        super().__init__(web3_conn_id,
                        ethereum_wallet,
                        gas_key,
                        gas,
                        gas_multiplier,
                        nonce, 
                        *args, 
                        **kwargs)
        self.router_address = router_address
        self.amount_in = amount_in
        self.amount_out_min = amount_out_min
        self.path = path
        self.to = to
        if not deadline:
            self.deadline = time() + 300
        else:
            self.deadline = deadline
        self.abi_json = SWAP_ABI

    def execute(self, context):
        # Create the contract factory
        print("Processing distribution for Ricochet at {0} by EOA {1}".format(
            self.contract_address, self.wallet.public_address
        ))

        transaction_hash = super().transact(self.contract_address, 
                                            self.abi_json, 
                                            'swapExactTokensForEth', 
                                            self.amount_in, 
                                            self.amount_out_min, 
                                            self.path, self.to, 
                                            int(self.deadline))

        # contract = self.web3.eth.contract(self.contract_address, abi=self.abi_json)
        # # Form the signed transaction
        # withdraw_txn = contract.functions.swapExactTokensForETH(self.amount_in,
        #                                                         self.amount_out_min,
        #                                                         self.path,
        #                                                         self.to,
        #                                                         int(self.deadline))\
        #                                  .buildTransaction(dict(
        #                                    nonce=int(self.nonce),
        #                                    gasPrice = int(self.web3.eth.gasPrice *\
        #                                               self.gas_multiplier),
        #                                    gas = self.gas
        #                                   ))
        # signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # # Send the transaction
        # transaction_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Sent swapExactTokensForETH({self.amount_in},{self.amount_out_min},{self.path},{self.to},{self.deadline})... transaction hash: {transaction_hash.hex()}")
        return str(transaction_hash.hex()) # Return for use with EthereumTransactionConfirmationSensor
