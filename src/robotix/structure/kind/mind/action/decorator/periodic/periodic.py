from mathx.numbers.kind.real.interval.interval import Interval
from robotix.structure.kind.mind.action.decorator.decorator import Decorator


class Periodic(Decorator):
    def __init__(self, time_interval:Interval):
        self._time_interval = time_interval

    def get_time_interval(self):
        return self._time_interval