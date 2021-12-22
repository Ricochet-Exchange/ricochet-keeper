from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import RICOCHET_ABI


class RicochetStreamerCloseOperator(ContractInteractionOperator):
    """
    Closes a streamers stream using `closeStream`
    """
    template_fields = ['streamer_address', 'exchange_address']
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 streamer_address,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.streamer_address = streamer_address
        self.abi_json = RICOCHET_ABI
        self.function = self.contract.functions.closeStream

    def execute(self, context):
        self.function_args = {"streamer": self.streamer_address}
        return super().execute(context)
