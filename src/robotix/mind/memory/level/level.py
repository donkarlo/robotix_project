from utilix.data.storage.interface import Interface as DataStorageProto

class Level:
    """
    Each level is Level should have access to hardware for saving data on it and have ram to keep it in its active memory
    """
    def __init__(self, storage: DataStorageProto):
        self._storage = storage