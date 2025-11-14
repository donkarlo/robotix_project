from robotix.mind.memory.composite.composite import Composite as MemoryTree
from robotix.mind.memory.trace.trace import Trace
from robotix.mind.memory.composite.observer.trace.creation_subscriber import \
    TraceCreationSubscriber as TraceCreationSubcriber
from robotix.mind.memory.memorizing.memorizing import Memorizing
from robotix.mind.memory.remembering.remembering import Remembering
from robotix.mind.memory.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import override, List


class Memory(TraceCreationSubcriber):


    def __init__(self, memory_tree:MemoryTree, memorizing:Memorizing, remembering:Remembering):
        """
        Here we design the aritecture or philosophy of the memory. The body part is in body
        coupling memorizing, remebering and storing
        Args:
            memory_tree

        """
        self._memorizing = memorizing
        self._remembering = remembering

        self._set_memory_tree(memory_tree)

    def get_remembering(self)->Remembering:
        return self._remembering

    def get_memorizing(self) -> Memorizing:
        return self._memorizing

    def get_memory_tree(self)-> ExperienceGroup:
        return self._memory_tree

    def _set_memory_tree(self, experience_group: ExperienceGroup)->None:
        """
        Returns:
        """
        self._memory_tree = experience_group
        self._memorizing.set_memory_tree(self._memory_tree)
        self._remembering.set_memory_tree(self._memory_tree)

    def recieve_traceable(self, traceable: Traceable):
        """
        something that has the potential to be a memorizable trace
        Returns:

        """
        pass

    def decide_memorizable(self):
        pass




