from abc import abstractmethod
from robotix.memory.provoker import Provoker
from utilityx.data.source.source import Source
from robotix.memory.remembering import Remembering as RememberingBase


class Remembering(RememberingBase):
    """The action of remebering by an evidence, episode or sequence of observation or just will"""
    def __init__(self, provoker:Provoker):
        """It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class"""
        pass

    @abstractmethod
    def remember(self, piece:Provoker)->Provoker:
        pass