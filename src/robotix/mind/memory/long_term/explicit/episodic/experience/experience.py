from robotix.mind.memory.long_term.explicit.episodic.experience.level.level import Level
from robotix.mind.memory.long_term.explicit.episodic.experience.level.stack.stack import Stack
from robotix.mind.goal.composite.mission.mission import Mission
from robotix.mind.action.composite.plan.plan import Plan
from typing import Optional



class Experience:
    def __init__(self, mission:Mission, executed_plan:Plan, level_stack:Stack, name:Optional[str]=None):
        """
        Unlike scenario, you dont need world here, all is in experience current_level 0 about world understanding of the robot. Scenario is human view for testing
        Args:
            mission:
            executed_plan:
            level_stack: for example current_level 0 is sensory data, current_level 1 is clusters
        """
        # initial pre_plan
        self._mission = mission
        self._executed_plan = executed_plan
        self._level_stack = level_stack
        self.__name = name

    def get_level_stack(self) -> Stack:
        return self._level_stack

    def get_name(self) -> Optional[str]:
        return self.__name

    def get_lowest_level(self)->Level:
        return self._level_stack.get_lowest_level()

    def build_upper_level(self, current_level:Level)->None:
        pass
