from mathx.linalg.matrix.vec.col_vec import ColVec


class State:
    def __init__(self, vec:ColVec):
        self._vec:ColVec = vec