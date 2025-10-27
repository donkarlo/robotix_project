from robotix.cognition.mind.memory.episode.experience import Experience
from robotix.cognition.mind.memory.memorizing import Memorizing
from robotix.cognition.mind.memory.remembering import Remembering
from robotix.cognition.mind.memory.episode.experience_set import ExperienceSet
from typing import Optional


class Memory:
    def __init__(self, memorizing:Memorizing, remembering:Remembering, experience_set:Optional[ExperienceSet]=None):
        """
        coupling memorizing, remebering and storing
        Args:

        """
        self._memorizing = memorizing
        self._remembering = remembering

        if ExperienceSet is not None:
            self._experience_set = experience_set
        else:
            self._experience_set = ExperienceSet()

        self.set_experience_set(experience_set)


    def get_memorizing(self)->Memorizing:
        return self._memorizing

    def get_remembering(self)->Remembering:
        return self._remembering

    def get_experience_set(self)->ExperienceSet:
        return self._experience_set

    def set_experience_set(self, experience_set:ExperienceSet)->None:
        """
        Returns:
        """
        self._experience_set = experience_set
        self._memorizing.set_experience_set(self._experience_set)
        self._remembering.set_experience_set(self._experience_set)

    def add_experience(self, experience:Experience)->None:
        self._experience_set.add_child(experience)
