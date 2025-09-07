from robotix.mind.memory.memorizing import Memorizing as MemorizingBase


class Memorizing(MemorizingBase):
    """
    - The storage place will be detrmined
    """
    def __init__(self, source:Source):
        self._source = source

    def memorize(self)->bool:
        """"""
        pass

