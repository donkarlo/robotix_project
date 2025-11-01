from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace import Trace
from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace_arrival_observer_interface import \
    TraceArrivalObserverInterface
from robotix.mental.cognition.memory.memorizing import Memorizing
from robotix.mental.cognition.memory.remembering import Remembering
from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.collection.collection import \
    Collection as ExperienceCollection
from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import Optional, override


class Memory(TraceArrivalObserverInterface):
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

    @override
    def do_with_arrived_trace(self, trace: Trace) -> None:
        self.get_remembering().do_with_arrived_trace(trace)
        self.get_memorizing().do_with_arrived_trace(trace)
