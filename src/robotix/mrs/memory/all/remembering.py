from abc import abstractmethod

from robotix.memory.piece import Piece
from utilityx.data.source.source import Source


class Remembering:
    """The action of remebering by an evidence, episode or sequence of observation or just will"""
    def __init__(self, piece:Piece):
        """It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class"""
        pass

    @abstractmethod
    def remember(self, piece:Piece)->Piece:
        pass