from typing import List

from abc import abstractmethod

from sensorx.sensor_set import SensorSet

from robotix.mind.memory.episode.episode import Episode
from robotix.mind.memory.level.levels import Levels
from robotix.mind.memory.trigger import Trigger


class Remembering:
    """
    This class abstracts a strategy for remebering
    The act of remebering by an evidence, episode or sequence of observation or just will
    - remembering is the process of bringing (meaningful) data from long-term memory
    """
    def __init__(self):
        """
        It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class
        """
        self._levels = None

    def set_levels(self, levels: Levels)-> None:
        self._levels = levels

    @abstractmethod
    def remember(self, trigger:Trigger)->None:
        """
        This is unintentionall
        Args:
            trigger:

        Returns:

        """
        pass

    @abstractmethod
    def recall(self):
        """intentional"""
        pass