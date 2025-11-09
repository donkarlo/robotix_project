from robotix.mind.memory.trace.trace import Trace
from robotix.mind.memory.trace.observer.creation_subscriber import \
    CreationSubscriber as TraceCreationSubcriber
from robotix.mind.memory.memorizing.memorizing import Memorizing
from robotix.mind.memory.remembering.remembering import Remembering
from robotix.mind.memory.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from typing import override, List


class Memory(TraceCreationSubcriber):
    def get_memorizing(self)->Memorizing:
        return self._memorizing


    def __init__(self, experience_group: ExperienceGroup, memorizing:Memorizing, remembering:Remembering):
        """
        Here we design the aritecture or philosophy of the memory. The body part is in body
        coupling memorizing, remebering and storing
        Args:
            experience_group

        """
        self._experience_group = experience_group
        self._memorizing = memorizing
        self._remembering = remembering

        self.set_experience_collection(experience_group)

    def get_remembering(self)->Remembering:
        return self._remembering

    def get_experience_collection(self)->ExperienceCollection:
        return self._experience_group

    def set_experience_collection(self, experience_collection:ExperienceCollection)->None:
        """
        Returns:
        """
        self._experience_group = experience_collection
        self._memorizing.set_experience_collection(self._experience_group)
        self._remembering.set_experience_collection(self._experience_group)

    def add_experience(self, experience:Experience)->None:
        self._experience_group.add_child(experience)

    @override(TraceCreationSubcriber)
    def do_with_created_trace(self, trace: Trace) -> None:
        self.get_remembering().do_with_arrived_trace(trace)
        self.get_memorizing().do_with_created_trace(trace)

    def review(self):
        experiences:List[Experience] = self.get_experience_collection().get_members()
        for experience in experiences:
            for modality in experience.get_modality_collection().get_members():
                for layer in modality.get_stack().get_layers():
                    if layer.get_storage() is not None:
                        if layer is upper_buildable:
                            layer.build_next_upper_layer()


