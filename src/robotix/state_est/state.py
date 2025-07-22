from mathx.linalg.matrix.vec.col_vec import ColVec


class State:
    '''
    This version talks only about robots. Later we can have something from cntrol theory
    '''
    def __init__(self, vec:ColVec):
        self._vec:ColVec = vec