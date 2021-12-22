from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import REX_BANK_ABI
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

class RexBankDepositOperator(ContractInteractionOperator):
    template_fields = ['amount']
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 amount,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.amount = amount
        self.abi_json = REX_BANK_ABI
        self.function = self.contract.functions.vaultDeposit

    def execute(self, context):
        self.function_args = {"amount": int(self.amount)}
        return super().execute(context)
