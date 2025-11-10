from abc import abstractmethod
from robotix.mind.memory.force import Force
from robotix.mind.memory.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.mind.memory.long_term.explicit.episodic.experience.experience import Experience


class Remembering:
    """
    This class abstracts a strategy for remebering
    The role of remebering by an evidence, episodic or sequence of observation or just will
    - remembering is the process of bringing (meaningful) data from long-term memory
    """
    def __init__(self, order):
        """
        It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class
        """
        self._levels = None

    def set_experience_group(self, experience_group: ExperienceGroup) -> None:
        self._experience_group = experience_group

    @abstractmethod
    def remember(self, force:Force)->None:
        """
        This is unintentionall
        Args:
            force:

        Returns:

        """
        pass

    @abstractmethod
    def recall(self, force:Force)->None:
        """
        intentional
        """
        pass

    def recall_experience_by_experience_name(self, experience_name:str)->Experience:
        return self._experience_group.get_experience_by_name(experience_name)
