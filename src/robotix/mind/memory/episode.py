from abc import abstractmethod
from utilityx.data.source.unit import Unit


class  Episode(Unit):
    """
    Maybe different from Trigger, I should think about it
    - from what an episode must be composed
        − Goal
            - action (with feed back)
                - commands (one time signals to actuators)
            - sensors
    """
    def __init__(self):
        pass

    @abstractmethod
    def get_string(self):
        pass
