from physix.quantity.kind.time import Time
from robotix.mind.memory.trace.decorator.decorator import Decorator
from robotix.mind.memory.trace.interface import Interface as TraceInterface


class Timed(Decorator):
    def __init__(self, inner: TraceInterface, time:Time):
        Decorator.__init__(self, inner)
        self._time = time
    def get_time(self)->Time:
        return self._time
