
from robotix.mind.goal.composite.mission.mission import Mission
from robotix.mind.action.composite.plan.plan import Plan
from typing import Optional

from robotix.mind.memory.long_term.explicit.experience.modality.collection.collection import Collection as ModalityCollection


class Experience:
    def __init__(self, modality_collection: ModalityCollection, mission:Mission, executed_plan:Plan, name:Optional[str]=None):
        """
        Unlike scenario, you dont need world here, all is in experience current_level 0 about world understanding of the robot. Scenario is human view for testing
        Args:
            mission:
            executed_plan:
            modality_collection: for example current_level 0 is sensory data, current_level 1 is clusters
        """
        # initial pre_plan
        self._modality_collection = modality_collection
        self._mission = mission
        self._executed_plan = executed_plan
        self.__name = name

    def get_modality_collection(self) -> ModalityCollection:
        return self._modality_collection

    def get_name(self) -> Optional[str]:
        return self.__name

    def find_cycles(self):
        pass
