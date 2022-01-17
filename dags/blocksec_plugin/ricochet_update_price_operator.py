from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import UPDATE_TOKEN_PRICE_ABI

class RicochetUpdatePriceOperator(ContractInteractionOperator):
    """
    Calls `updateTokenPrice` on Ricochet contracts
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 token_address,
                 *args,
                 **kwargs):
        super().__init__(abi_json=UPDATE_TOKEN_PRICE_ABI, *args, **kwargs)

    def execute(self, context):
        self.function_args = {"_token": token_address}
        self.function = self.contract.functions.updateTokenPrice
        return super().execute(context)
