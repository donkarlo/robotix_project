from typing import List
from robotix.mind.memory.episode.episode import Episode
from robotix.mind.memory.storage.storage import Storage


class Memorizing:
    """
    - The storage place will be detrmined
    """
    def __init__(self):
        #should be set by calling set storage from Memory class
        self._storage = None

    def memorize(self, episodes:List[Episode])->bool:
        """
        What entities exist to memorize

        """
        return False

    def set_storage(self, storage: Storage) -> None:
        self._storage = storage

