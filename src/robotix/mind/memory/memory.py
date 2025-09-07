from robotix.mind.memory.memorizing import Memorizing
from robotix.mind.memory.remembering import Remembering


class Memory:
    def __init__(self, memorizing:Memorizing, remembering:Remembering, storage:Storage):
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
