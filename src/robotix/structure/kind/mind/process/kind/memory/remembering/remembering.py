from abc import abstractmethod
from robotix.mind.cognition.process.kind.memory.force import Force
from robotix.mind.cognition.process.kind.memory.kind.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.mind.cognition.process.kind.memory.kind.long_term.explicit.episodic.experience.experience import Experience


class Remembering:
    """
    This class abstracts a strategy for remebering
    The role of remebering by an evidence, episodic or sequence of observation or just will
    - remembering is the process of bringing (meaningful) pair_set from long-term memory
    - remebering is always to reduce the suprise as much as possible. we remeber to make our prediction system better
    """
    def __init__(self, order):
        """
        It is not necessary to set the pair_set os_file as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Working class
        """
        self._levels = None

    def set_memory_tree(self, experience_group: ExperienceGroup) -> None:
        self._experience_group = experience_group

    @abstractmethod
    def remember(self, force:Force)->None:
        """
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

    def review(self):
        #TODO: traverse from leaves to roots
        tree: List[Experience] = self.get_memory_tree().get_members()

