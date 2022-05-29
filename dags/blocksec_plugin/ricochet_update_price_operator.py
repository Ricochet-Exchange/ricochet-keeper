from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import UPDATE_TOKEN_PRICES_ABI

class RicochetUpdatePriceOperator(ContractInteractionOperator):
    """
    Calls `updateTokenPrices` on Ricochet contracts
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(abi_json=UPDATE_TOKEN_PRICES_ABI, *args, **kwargs)

    def execute(self, context):
        self.function = self.contract.functions.updateTokenPrices
        return super().execute(context)
