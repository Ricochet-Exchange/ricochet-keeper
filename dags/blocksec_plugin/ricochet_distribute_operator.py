from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import DISTRIBUTE_ABI

class RicochetDistributeOperator(ContractInteractionOperator):
    """
    Calls `distribute` on Ricochet contracts
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.abi_json = DISTRIBUTE_ABI
        self.argsForFunction = {}
        self.function = self.contract.functions.distribute