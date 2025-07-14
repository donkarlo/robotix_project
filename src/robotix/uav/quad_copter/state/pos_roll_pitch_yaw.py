from mathx.linalg.matrix.vec.col_vec import ColVec
from mathx.linalg.matrix.vec.position.three_d_col_vec import ThreeDColVec
from src.robotix.State import State


class PosRollPitchYaw(State):
    def __init__(self, pos:ThreeDColVec, roll:float, pitch:float, yaw:float):
        '''

        Args:
            pos:
            roll: radian
            pitch: radian
            yaw: radian
        '''
        self._pos:ThreeDColVec = pos
        self._roll:float = roll
        self._pitch:float = pitch
        self._yaw:float = yaw
        super().__init__(pos.extend_vertically(ColVec(roll, pitch, yaw)))
