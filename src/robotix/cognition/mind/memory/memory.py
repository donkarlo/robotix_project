from robotix.cognition.mind.memory.memorizing import Memorizing
from robotix.cognition.mind.memory.remembering import Remembering
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.collection.collection import \
    Collection as ExperienceCollection
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import Optional


class Memory:
    def __init__(self, memorizing:Memorizing, remembering:Remembering, experience_collection:Optional[
        ExperienceCollection]=None):
        """
        coupling memorizing, remebering and storing
        Args:

        """
        self._memorizing = memorizing
        self._remembering = remembering

        if ExperienceCollection is not None:
            self._experience_collection = experience_collection
        else:
            self._experience_collection = ExperienceCollection()

        self.set_experience_collection(experience_collection)


    def get_memorizing(self)->Memorizing:
        return self._memorizing

    def get_remembering(self)->Remembering:
        return self._remembering

    def get_experience_collection(self)->ExperienceCollection:
        return self._experience_collection

    def set_experience_collection(self, experience_collection:ExperienceCollection)->None:
        """
        Returns:
        """
        self._experience_collection = experience_collection
        self._memorizing.set_experience_collection(self._experience_collection)
        self._remembering.set_experience_collection(self._experience_collection)

    def add_experience(self, experience:Experience)->None:
        self._experience_collection.add_child(experience)
