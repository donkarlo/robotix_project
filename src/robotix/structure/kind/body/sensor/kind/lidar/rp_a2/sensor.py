from mathx.linalg.tensor.vector.vector import Vector
from physix.dimension.unit.scalar import Scalar
from physix.dimension.unit.unit import Unit
from robotix.structure.kind.body.sensor.sensor import Sensor as BasicSensor

class Sensor(BasicSensor):
    # vector dim is 720
    def __init__(self):
        freq = Scalar(Unit("hz"), 98.95)
        super().__init__("lidar", freq, "rp_a2")

    def validate_observation(self, ranges:Vector)->bool:
        return True