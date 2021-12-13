from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import VAULT_DEPOSIT_ABI
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
        self.function_args = {"amount": self.amount}
        self.function = self.contract.functions.vaultDeposit