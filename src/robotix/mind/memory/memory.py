from robotix.mind.memory.long_term.explicit.episodic.trace.trace import Trace
from robotix.mind.memory.long_term.explicit.episodic.trace.trace_arrival_observer_interface import \
    TraceArrivalObserverInterface
from robotix.mind.memory.memorizing.memorizing import Memorizing
from robotix.mind.memory.remembering.remembering import Remembering
from robotix.mind.memory.long_term.explicit.episodic.experience.collection.collection import \
    Collection as ExperienceCollection
from robotix.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import override


class Memory(TraceArrivalObserverInterface):
    def get_memorizing(self)->Memorizing:
        return self._memorizing


    def __init__(self, initial_experience_collection: ExperienceCollection, memorizing:Memorizing, remembering:Remembering):
        """
        Here we design the aritecture or philosophy of the memory. The body part is in body
        coupling memorizing, remebering and storing
        Args:

        """
        self._initial_experience_collection = initial_experience_collection
        self._memorizing = memorizing
        self._remembering = remembering

        self.set_experience_collection(initial_experience_collection)

    def get_remembering(self)->Remembering:
        return self._remembering

    def get_experience_collection(self)->ExperienceCollection:
        return self._initial_experience_collection

    def set_experience_collection(self, experience_collection:ExperienceCollection)->None:
        """
        Returns:
        """
        self._initial_experience_collection = experience_collection
        self._memorizing.set_experience_collection(self._initial_experience_collection)
        self._remembering.set_experience_collection(self._initial_experience_collection)

    def add_experience(self, experience:Experience)->None:
        self._initial_experience_collection.add_child(experience)

    @override
    def do_with_arrived_trace(self, trace: Trace) -> None:
        self.get_remembering().do_with_arrived_trace(trace)
        self.get_memorizing().do_with_arrived_trace(trace)


