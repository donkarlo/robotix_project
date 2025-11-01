from physix.dimension.unit.scalar import Scalar
from robotix.mental.cognition.ontology.message.interface import Interface

class Timed(Decorator):
    def __init__(self, inner:Interface, time:Scalar):
        self._time = time
        super().__init__(inner)
    def get_time(self)->Time:
        return self._time