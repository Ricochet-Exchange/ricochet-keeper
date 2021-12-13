from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import HARVEST_ABI

class RicochetHarvestOperator(ContractInteractionOperator):
    """
    Calls `harvest` on Ricochet contracts
    """
    template_fields = []

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.abi_json = HARVEST_ABI
        self.argsForFunction = {}
        self.function = self.contract.functions.harvest
