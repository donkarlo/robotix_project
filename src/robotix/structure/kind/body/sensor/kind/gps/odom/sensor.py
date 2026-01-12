from physix.dimension.unit.scalar import Scalar
from robotix.structure.kind.body.sensor.sensor import Sensor as BasicSensor
from mathx.linalg.tensor.vector.vector import Vector
from physix.dimension.unit.unit import Unit

class Sensor(BasicSensor):
    """
    Odometry GPS is an odometry that its os_file was GPS and then GPS was fused with IMU or FCU
    """
    def __init__(self, id:int=None):
        freq= Scalar(Unit("hz"), 98.95)
        super().__init__("lidar", freq, "odom_gps")

    def validate_observation(self, observation: Vector) -> bool:
        return True