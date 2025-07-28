from mathx.linalg.matrix.vec.col_vec import ColVec
from robotix.type.uav.quad_copter.cmd import Cmd

class GoTo(Cmd):
    def __init__(self, pos:ColVec):
        self._pos = pos