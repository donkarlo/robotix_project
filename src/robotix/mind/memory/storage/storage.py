from typing import List

from abc import abstractmethod

from robotix.mind.memory.storage.level.level import Level


class Storage:
    def __init__(self, leavels:List[Level]):
        self._levels = leavels

    @abstractmethod
    def save_by_unit(self)->None:
        pass

    @abstractmethod
    def load(self)->None:
        pass