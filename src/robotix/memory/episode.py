from abc import abstractmethod, ABC
from utilityx.data.source.unit import Unit


class  Episode(Unit):
    """
    Maybe different from Provoker, I should think about it
    - from what a unit musxt eb composed
        - actions (with feed back)
        - commands (one time signals to actuators)
        - sensors
    """
    def __init__(self):
        pass

    @abstractmethod
    def get_string(self):
        pass
