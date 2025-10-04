from typing import List

from abc import abstractmethod

from robotix.mind.memory.storage.level.level import Level


class Storage:
    def __init__(self, levels:List[Level]):
        self._levels = levels

    @abstractmethod
    def save_by_episode(self)->None:
        pass

    @abstractmethod
    def load(self)->None:
        pass