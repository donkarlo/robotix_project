from abc import abstractmethod
from robotix.cognition.mind.memory.trigger import Trigger
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.collection.collection import Collection as ExperienceCollection


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

    def set_experience_collection(self, experience_collection: ExperienceCollection) -> None:
        self._experience_set = experience_collection

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