from abc import abstractmethod
from robotix.cognition.mind.memory.trigger import Trigger
from robotix.cognition.mind.memory.episode.experience_set import ExperienceSet


class Remembering:
    """
    This class abstracts a strategy for remebering
    The act of remebering by an evidence, episodic or sequence of observation or just will
    - remembering is the process of bringing (meaningful) data from long-term memory
    """
    def __init__(self):
        """
        It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class
        """
        self._levels = None

    def set_experience_set(self, experience_set: ExperienceSet) -> None:
        self._experience_set = experience_set

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