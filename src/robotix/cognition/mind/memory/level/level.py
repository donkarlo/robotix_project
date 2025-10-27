from utilix.data.storage.interface import Interface as DataStorageProto
from typing import List

class Level:
    """
    Each level is Level should have access to hardware for saving data on it and have ram to keep it in its active memory
    """
    def __init__(self, storage: DataStorageProto):
        """
        Every experience has its own storage. a level can be formed of multiple experiences. now we just know storages for experiences. That is an experience
        Args:
            storage:
        """
        self._storage = storage

    def get_storage(self) -> DataStorageProto:
        return self._storage