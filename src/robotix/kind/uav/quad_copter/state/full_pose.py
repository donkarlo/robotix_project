from mathx.linalg.matrix.vec.col_vec import ColVec
from mathx.linalg.matrix.vec.position.three_d_col_vec import ThreeDColVec
from robotix.state_est.state import State


class FullPose(State):
    def __init__(self, pos:ThreeDColVec, height:height, roll:float, pitch:float, yaw:float):
        '''
        Fill in with best estimation which is done out of here.
        it is not a place for estimation. it is just to hold separated group.
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
