from typing import List

from abc import abstractmethod

from sensorx.sensor_set import SensorSet

from robotix.mind.memory.episode.episode import Episode
from robotix.mind.memory.storage.storage import Storage
from robotix.spa.plan.goal.goal import Goal
class Remembering:
    """
    This class abstracts a strategy for remebering
    The action of remebering by an evidence, episode or sequence of observation or just will
    - remembering is the process of bringing (meaningful) data from long-term memory
    """
    def __init__(self):
        """
        It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class
        """
        self._storage = None

    def set_storage(self, storage: Storage)-> None:
        self._storage = storage

    @abstractmethod
    def remember(self, observed_episodes:List[Episode])->None:
        pass



    def load(self):
        pass