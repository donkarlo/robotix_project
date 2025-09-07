from sensorx.sensor import Sensor as BaseSensor
from sensorx.sensor_set import SensorSet
from sensorx.type.type import Type


class Sensor(BaseSensor):
    def __init__(self, type:int, freq:UnitedScalarVal, id:int=None):
        super().__init__(type, freq)