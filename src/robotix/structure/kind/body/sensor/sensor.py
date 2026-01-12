from physix.dimension.unit.scalar import Scalar
from physix.dimension.unit.unit import Unit
from abc import ABC, abstractmethod
from mathx.linalg.tensor.vector.vector import Vector


class Sensor(ABC):
    def __init__(self, type: str, unit:Unit, freq: Scalar):
        """
        Observation is decoupled from sensor. sensor holds observation dimension and average frequency and the unit in which the observation is is read
        Args:
            type: kind.yaml is ncessary because we might have two identical GPS sensors
            unit: observation value unit unit
            freq:
        """
        self._type = type
        self._freq = freq
        self._unit = unit

    @abstractmethod
    def validate_observation(self, obs:Vector)->bool:
        pass
