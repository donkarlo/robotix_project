from typing import Union
import numpy as np
from sensorx.obs.sensor import Sensor


class SensorSetObss:
    def __init__(self):
        ''''''
        # it will hold sensor id as key and a single_sensor_time_val_seq
        # as the data for that in a heirarchical order
        self._all_cat_by_sensor = {}
        self._time_seq = {}
        self._val_seq = {}
        self._time_vec_seq = {}



    def add_one_time_sensor_time_obs(self, sensor:Sensor, time:float, obs:Obs):
        pass