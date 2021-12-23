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
        super().__init__(abi_json=REX_BANK_ABI, *args, **kwargs)
        self.amount = amount

    def execute(self, context):
        self.initContract()
        self.function_args = {"amount": int(self.amount)}
        self.function = self.contract.functions.vaultDeposit
        return super().execute(context)
