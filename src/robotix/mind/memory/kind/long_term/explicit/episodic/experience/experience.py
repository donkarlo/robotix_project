
from robotix.mind.goal.composite.mission.mission import Mission
from robotix.mind.action.composite.plan.plan import Plan
from typing import Optional

from robotix.mind.memory.kind.long_term.modality.group.group import Group as ModalityCollection
from robotix.mind.memory.stack.stack import Stack


class Experience:
    def __init__(self, mission: Mission, executed_plan: Plan, shared_stack:Stack, modality_group: ModalityCollection, name:Optional[str]=None):
        """
        https://en.wikipedia.org/wiki/Experience
        Unlike scenario, you dont need world here, all is in experience current_level 0 about world understanding of the robot. Scenario is human view for testing
        Args:
            mission:
            executed_plan:
            shared_stack: all modalities are in a trace_storage file
            modality_group: for example current_level 0 is sensory data, current_level 1 is clusters
        """
        # initial pre_plan
        self._shared_stack = shared_stack
        self._modality_collection = modality_group
        self._mission = mission
        self._executed_plan = executed_plan
        self.__name = name

    def get_modality_collection(self) -> ModalityCollection:
        return self._modality_collection

    def get_name(self) -> Optional[str]:
        return self.__name

    def find_cycles(self):
        pass
