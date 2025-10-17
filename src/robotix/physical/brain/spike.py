from mathx.numbers.real.interval.interval import Interval
from physix.dimension.unit.unit import Unit


class Spike:
    """
    electrical load sent to brain or recived from brain
    - it is not curvy, it goes up suddenly and comes down suddenly
    """
    def __init__(self, time_interval:Interval, time_unit:Unit, voltage_interval:Interval, voltage_unit:Unit):
        self.time_interval = time_interval
        self.time_unit = time_unit
        self.voltage_interval = voltage_interval
        self.voltage_unit = voltage_unit