from sensorx.sensor import Sensor as BaseSensor
from sensorx.type.type import Type

class Sensor(SensorBase):
    def __init__(self, type:int, freq:UnitedScalarVal):
        super().__init__(type, freq)