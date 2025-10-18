from physix.dimension.unit.scalar import Scalar
from robotix.mind.language.message.interface import Interface

class Timed(Decorator):
    def __init__(self, inner:Interface, time:Scalar):
        self._time = time
        super().__init__(inner)
    def get_time(self)->Time:
        return self._time