from mathx.linalg.vec.opr.many_operanded import ManyOperanded
from mathx.linalg.vec.vec import Vec
from typing import List

class State(Vec):
    """
    State is a set of vectors as variables which are contributing to the predicting the next state of a system.
    for example in a physical system
    """
    def __init__(self, vecs:List[Vec]):
        self._vecs = vecs
        super().__init__(ManyOperanded(self._vecs).get_concated())

    def get_vec(self)-> List[Vec]:
        return self._vecs
