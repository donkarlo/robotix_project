from physix.kinematics.pose import Pose


class Odometry:
    def __init__(self, sensor_set_vals: SensorSetVals):
        self._sensor_set_vals:SensorSetVals = sensor_set_vals

    def get_pose(self)->Pose:
        pass