from robotix.mind.memory.memorizing import Memorizing as MemorizingBase


class Memorizing(MemorizingBase):
    """
    - The _levels place will be detrmined
    """
    def __init__(self, source:Source):
        self._source = source

    def memorize(self)->bool:
        """"""
        pass

