from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import SUPERTOKEN_ABI
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

class SuperTokenDowngradeOperator(ContractInteractionOperator):
    """
    Downgrades a supertoken
    """
    template_fields = ['amount']
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 amount,
                 *args,
                 **kwargs):
        super().__init__(abi_json=SUPERTOKEN_ABI, *args, **kwargs)
        self.amount = amount

    def execute(self, context):
        if int(self.amount) < 0:
            # Max downgrade
            self.amount = contract.functions.balanceOf(self.wallet.public_address).call()
        self.function = self.contract.functions.downgrade
        self.function_args = {"amount": int(self.amount)}
        return super().execute(context)
