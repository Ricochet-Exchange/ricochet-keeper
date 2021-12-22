from airflow.utils.decorators import apply_defaults
from blocksec_plugin.abis import SHARE_PRICE_ABI
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

class RicochetLaunchpadPrice(ContractInteractionOperator):
    """
    Checks the price of a Ricochet Launchpad
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.abi_json = SHARE_PRICE_ABI
        self.function_args = {}
        self.function = self.contract.functions.getSharePrice