from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import REX_BANK_ABI
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

class RexBankUpdateCollateralPriceOperator(ContractInteractionOperator):
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(abi_json=REX_BANK_ABI, *args, **kwargs)

    def execute(self, context):
        self.function_args = {}
        self.function = self.contract.functions.updateCollateralPrice
        return super().execute(context)
