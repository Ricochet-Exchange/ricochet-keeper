from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.hooks.postgres_hook import PostgresHook


class RicochetStreamerListOperator(BaseOperator):
    """
    Checks for all UpdatedStream events on Ricochet and saves them into a file
    """
    template_fields = []
    ui_color = "#ADF5FF"

    @apply_defaults
    def __init__(self,
                 state_file_path='state.json',
                 postgres_conn_id='data_warehouse',
                 contract_address=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.postgres_conn_id = postgres_conn_id
        self.contract_address = contract_address
        self.state_file_path = state_file_path


    def execute(self, context):

        execution_date = context['execution_date'].isoformat()
        sql = """
        select distinct args->>'from'
        from ethereum_events
        where event = 'UpdatedStream' and address = '{0}'
        """.format(self.contract_address)
        print(sql)
        postgres = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        conn = postgres.get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        addresses = []
        for result in results:
            print("Found Address", result[0])
            addresses.append(result[0])

        return addresses
