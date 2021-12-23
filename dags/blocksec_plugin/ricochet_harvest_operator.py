from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import HARVEST_ABI

class RicochetHarvestOperator(ContractInteractionOperator):
    """
    Calls `harvest` on Ricochet contracts
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(abi_json=HARVEST_ABI, *args, **kwargs)
        self.function_args = {}
        self.function = self.contract.functions.harvest
