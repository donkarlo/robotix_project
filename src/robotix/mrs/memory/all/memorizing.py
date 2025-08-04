from robotix.memory.provoker import Provoker
from robotix.memory.memorizing import Memorizing as MemorizingBase


class Memorizing(MemorizingBase):
    """
    - The storage place will be detrmined
    """
    def __init__(self, source:Source):
        self._source = source

    def memorize(self)->bool:
        """"""
        pass

