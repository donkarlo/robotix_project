from joblib import Memory

from robotix.mind.cognition.process.kind.memory.composite.composite import Composite as MemoryTree
from robotix.mind.cognition.process.kind.memory.composite.observer.trace.creation_subscriber import \
    TraceCreationSubscriber as TraceCreationSubcriber
from robotix.mind.cognition.process.kind.memory.memorizing.memorizing import Memorizing
from robotix.mind.cognition.process.kind.memory.remembering.remembering import Remembering
from robotix.mind.cognition.process.kind.memory.kind.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.trace.interface import Interface


class Working(TraceCreationSubcriber):
    """
    To represent working memory
    """

    def __init__(self, memory_tree:MemoryTree, memorizing:Memorizing, remembering:Remembering):
        """
        Here we design the aritecture or philosophy of the memory. The body part is in body
        coupling memorizing, remebering and storing
        Args:
            memory_tree: contains short and long term memory tree
            memorizing: contains the strategy for memorizing something
            remembering: contains the strategy to remeber somethings

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

    def recieve_traceable(self, traceable: Interface):
        """
        something that has the potential to be a memorizable trace
        Returns:

        """
        pass

    def recieve_memory_component(self, memory_component: Memory):
        """
        something that has the potential to be a memorizable memory component
        Returns:

        """
        pass

    def decide_memorizable(self):
        pass

    def decide_segregation(self)->None:
        pass

    def decide_integration(self)->None:
        pass




