from sensorx.sensor import Sensor
from sensorx.obs.obs import SensorObs
from mathx.linalg.matrix.col_vec import ColVec


class Obs(SensorObs):
    def __init__(self, time:float, vec:ColVec):
        super().__init__(time, vec)
        #todo check 3d validity

