from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.web3_hook import Web3Hook
from blocksec_plugin.ethereum_wallet_hook import EthereumWalletHook

class ContractInteractionOperator(BaseOperator):
    """
    Supercedes other operators that interacts with contracts
    """
    template_fields = []
    
    @apply_defaults
    def __init__(self,
                price,
                streamer_address=None,
                exchange_address=None,
                contract_address=None,
                web3_conn_id='web3_default',
                ethereum_wallet=None,
                request_id=None,
                spender=None,
                amount=None,
                nonce=None,
                gas=1200000,
                gas_key="fast",
                gas_multiplier=1,
                *args,
                **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.streamer_address = streamer_address
        self.exchange_address = exchange_address
        self.contract_address = contract_address
        self.web3_conn_id = web3_conn_id
        self.ethereum_wallet = ethereum_wallet
        self.request_id = request_id
        self.spender = spender
        self.amount = amount
        self.gas = gas
        self.gas_key = gas_key
        self.gas_multiplier = gas_multiplier
        self.web3 = Web3Hook(web3_conn_id=self.web3_conn_id).http_client
        self.wallet = EthereumWalletHook(ethereum_wallet=ethereum_wallet)
        if nonce:
            self.nonce = nonce
        else: # Look up the last nonce for this wallet
            self.nonce = self.web3.eth.getTransactionCount(self.wallet.public_address)

    def transact(self, contract_address, abi, functionName, *args):
        contract = self.web3.eth.contract(contract_address, abi=abi)

        func = getattr(contract.functions, functionName)
        # form transaction with dynamic values
        withdraw_txn = func(*args).buildTransaction(dict(
            nonce=int(self.nonce),
            gasPrice=int(self.web3.eth.gasPrice * self.gas_multiplier),
            gas=self.gas
        ))

        signed_txn = self.web3.eth.account.signTransaction(withdraw_txn, self.wallet.private_key)
        # Send the transaction
        return self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)



# inherit init params that are the same throughout operators that call contract code

# make a generic execute method that takes in the function called and returns a transaction hash