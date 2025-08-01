from abc import ABC, abstractmethod
from robotix.memory.conf.conf import Conf
from robotix.memory.memorizing import Memorizing
from robotix.memory.provoker import Provoker
from utilityx.data.source.source import Source


class Memory(ABC):
    def __init__(self, source:Source, memorizing:Memorizing, remembering:Remebering):
        """
        This is to remeber
        Args:

        """
        self.__source = source
        self.__memorizing = memorizing
        self.__remembering = remembering


    def get_memorizing(self)->Memorizing:
        return self.__memorizing
