from robotix.mind.memory.memorizing import Memorizing
from robotix.mind.memory.remembering import Remembering
from robotix.mind.memory.level.levels import Levels


class Memory:
    def __init__(self, memorizing:Memorizing, remembering:Remembering, levels:Levels):
        """
        coupling memorizing, remebering and storing
        Args:

        """
        self._memorizing = memorizing
        self._remembering = remembering
        self._levels = levels

        self.__set_levels()


    def get_memorizing(self)->Memorizing:
        return self._memorizing

    def __set_levels(self)->None:
        """

        Returns:

        """
        self._memorizing.set_levels(self._levels)
        self._remembering.set_levels(self._levels)
