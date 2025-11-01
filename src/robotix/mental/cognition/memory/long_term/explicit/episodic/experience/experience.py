from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.level.level import Level
from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.level.stack.stack import Stack
from robotix.plan.mission.mission import Mission
from robotix.plan.plan import Plan
from typing import Optional



class Experience:
    def __init__(self, mission:Mission, executed_plan:Plan, level_stack:Stack, name:Optional[str]=None):
        """
        Unlike scenario, you dont need world here, all is in experience level 0 about world understanding of the robot. Scenario is human view for testing
        Args:
            mission:
            executed_plan:
            level_stack: for example level 0 is sensory data, level 1 is clusters
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
