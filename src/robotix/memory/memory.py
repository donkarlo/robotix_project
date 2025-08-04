from abc import ABC, abstractmethod
from robotix.memory.conf.conf import Conf
from robotix.memory.memorizing import Memorizing
from robotix.memory.provoker import Provoker


class Memory(ABC):
    def __init__(self, memorizing:Memorizing, membering:Remembering, storage:Storage):
        """
        coupling memorizing, remebering and storing
        Args:

        """
        self._storage = storage
        self._memorizing = memorizing
        self._remembering = remembering

        self.__set_storage()


    def get_memorizing(self)->Memorizing:
        return self._memorizing

    def __set_storage(self)->bool:
        self._memorizing.set_storage(self._storage)
        self._remembering.set_storage(self._storage)
        return True
