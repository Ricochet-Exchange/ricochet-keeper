from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from random import randrange
from time import sleep

class RandomSleepOperator(BaseOperator):
    """
    Sleep for a random amount of time
    """
    template_fields = []

    @apply_defaults
    def __init__(self,
                 min=None,
                 max=None,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.min = min
        self.max = max


    def execute(self, context):
        """
        Sleep for a random number of seconds
        """
        duration = randrange(self.min, self.max)
        sleep(duration)
