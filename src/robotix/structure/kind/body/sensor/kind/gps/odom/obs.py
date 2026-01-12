from robotix.structure.kind.body.sensor.sensor import Sensor
from robotix.structure.kind.body.sensor.observation.observation import Observation as SensorObs
from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from physix.dimension.unit.unit import Unit
from physix.kinematics.pose import Pose
from physix.kinematics.twist import Twist


class Obs(SensorObs):
    def __init__(self, sensor:Sensor, pose:Pose, pose_unit:Unit, twist:Twist, twist_unit:Unit):
        self._pose = pose
        self._pose_unit = pose_unit
        self._twist = twist
        self._twist_unit = twist_unit

        val = TwoOpranded(pose.get_components(), twist).concat()
        super().__init__(sensor, val)

