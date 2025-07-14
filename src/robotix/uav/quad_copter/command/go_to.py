from mathx.linalg.matrix.col_vec import ColVec

from src.robotix.command import Command


class GoTo(Command):
    def __init__(self, pos:ColVec):
        self._pos = pos