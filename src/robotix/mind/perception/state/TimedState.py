from robotix.mind.perception.state.state import State
from physix.dimension.unit import Scalar

class TimedState(State):
    def __init__(self, time:Scalar):
        self._time = time

    def get_time(self)->Scalar:
        return self._time