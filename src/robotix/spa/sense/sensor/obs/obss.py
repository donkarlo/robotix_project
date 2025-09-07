import numpy as np

from sensorx.sensor import Sensor
from sensorx.obs.obs import SensorTimeVec

from src.sensorx.obs.obs import Obs


class Obss:
    def __init__(self, sensor_id:int, obss:list[Obs,...]=None):
        self._sensor_id = sensor_id

        #initial goal_state
        self._obss_list = []

    def add_obs(self, obs:Obs):
        self._obss_list.append(obs)
