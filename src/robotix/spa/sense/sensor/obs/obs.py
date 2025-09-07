from typing import Union
import numpy as np
from mathx.linalg.matrix.col_vec import ColVec
from mathx.physics.dimension.unit.scalar import Scalar
from sensorx.sensor import Sensor


class Obs:
    '''
    For sensor, time, obs
    '''
    def __init__(self, sensor:Sensor , col_vec: ColVec, time:Scalar):
        self._time = time
        self._col_vec = col_vec
        self._sensor = sensor