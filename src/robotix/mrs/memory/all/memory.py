from abc import ABC, abstractmethod
from robotix.memory.conf.conf import Conf
from robotix.memory.memorizing import Memorizing
from robotix.memory.provoker import Provoker
from utilityx.data.source.source import Source
from robotix.memory.memorizing import Memory as MemoryBase


class Memory(MemoryBase):
    def __init__(self, source:Source, memorizing:Memorizing, remembering:Remebering):
        """
        In this method, I mean "all" method all the sensors etc are saved
        """
        self.__source = source
        self.__memorizing = memorizing
        self.__remembering = remembering


    def get_memorizing(self)->Memorizing:
        return self.__memorizing
