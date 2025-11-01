from mathx.numbers.real.interval.interval import Interval
from physix.dimension.unit.unit import Unit


class Spike:
    """
    electrical load sent to brain or recived from brain. about 1ms and 100 milli volts
    - it is not curvy, it goes up suddenly and comes down suddenly
    - another __name is role potential or nerve impulse
    - spike is formed of power (Voltage) and duration (Time)
    """
    def __init__(self, time_interval:Interval, time_unit:Unit, voltage_interval:Interval, voltage_unit:Unit):
        self.time_interval = time_interval
        self.time_unit = time_unit
        self.voltage_interval = voltage_interval
        self.voltage_unit = voltage_unit