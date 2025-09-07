from mathx.unit.united_scalar_val import UnitedScalarVal
from sensorx.sensor_set import SensorSet
from type.type import Type

class Sensor:
    def __init__(self, type:int, dim:int, freq:UnitedScalarVal):
        '''

        Args:
            type: come from sociomind
            dim:
            freq:
        '''
        self._type = type
        self._dim = dim
        self._freq = freq