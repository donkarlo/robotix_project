from typing import Union, Tuple
import numpy as np
from mathx.linalg.matrix.vec.col_vec import ColVec


class Point(State):
    def __init__(self, x:float, y:float, z:float):
        self._x = x
        self._y = y
        self._z = z
        super().__init__((self._x, self._y, self._z))