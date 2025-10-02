from utilix.data.storage.interface import Interface as DataStorage

class Level(DataStorage):
    """
    Each level is Level should have access to hardware for saving data on it and have ram to keep it in its active memory
    """
    def __init__(self, episode_components):
        self._episode_components = episode_components