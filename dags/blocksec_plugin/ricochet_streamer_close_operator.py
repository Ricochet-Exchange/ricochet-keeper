from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import REX_ABI


class RicochetStreamerCloseOperator(ContractInteractionOperator):
    """
    Closes a streamers stream using `closeStream`
    """
    template_fields = ['streamer_address', 'exchange_address', 'nonce']
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 streamer_address,
                 exhange_address,
                 *args,
                 **kwargs):
        super().__init__(abi_json=REX_ABI, *args, **kwargs)


    def execute(self, context):

        self.streamer_address = streamer_address
        self.exchange_address = exhange_address
        self.function = self.contract.functions.closeStream
        self.function_args = {"streamer": self.streamer_address}
        return super().execute(context)
