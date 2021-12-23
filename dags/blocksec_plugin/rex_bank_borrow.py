from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import REX_BANK_ABI, ERC20_ABI
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

class RexBankBorrowOperator(ContractInteractionOperator):

    template_fields = ['amount']
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 amount,
                 *args,
                 **kwargs):
        super().__init__(abi_json=REX_BANK_ABI, *args, **kwargs)
        self.amount = amount

    def execute(self, context):

        if int(self.amount) < 0:
            # Max borrow
            vault = contract.functions.vaults(self.wallet.public_address).call()
            print("vault",vault)
            price = contract.functions.getCollateralTokenPrice().call()
            price /= 1000000
            print("price", price)
            self.amount = vault[0] * price * 0.6 - vault[1]

        self.function = self.contract.functions.vaultBorrow
        self.function_args = {"amount": int(self.amount)}

        return super().execute(context)
