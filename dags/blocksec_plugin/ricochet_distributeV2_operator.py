from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator

DISTRIBUTE_ABI = """
[{"inputs":[{"internalType":"bytes","name":"ctx","type":"bytes"}],"name":"distribute","outputs":[{"internalType":"bytes","name":"newCtx","type":"bytes"}],"stateMutability":"nonpayable","type":"function"}]"""

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
        super().__init__(abi_json=DISTRIBUTE_ABI, *args, **kwargs)

    def execute(self, context):
        self.function_args = {"ctx": "0x"}
        self.function = self.contract.functions.distribute
        return super().execute(context)
