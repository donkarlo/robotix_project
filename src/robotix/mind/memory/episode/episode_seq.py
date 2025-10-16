from typing import List
from robotix.mind.memory.episode.episode import Episode
from utilix.data.storage.interface import Interface as StorageInterface

class EpisodeSeq:
    """
    A group of episodes some how got together either sequential or causal etc
    - An experience can be episodes
    """
    def __init__(self, episode_source:List[Episode]=None):
        self._episode_members = episode_source

    def add_sensor_set(self, sensor_set_vals:SensorSetObsVals):
        self._episode_members.append(sensor_set_vals)

    def get_episode_memebers(self) -> List[Episode]:
        return self._episode_members