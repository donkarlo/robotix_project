from robotix.mind.memory.level.level import Level
from robotix.mind.memory.level.level_stack import LevelStack
from robotix.mind.memory.episode.episode import Episode
from robotix.sense.world.world import World
from sensorx.obs.sensor_set_obs.sensor_set_obs_vals import SensorSetObsVals
from robotix.plan.mission.mission import Mission
from robotix.plan.plan import Plan
from typing import List, Optional



class Experience:
    def __init__(self, mission:Mission, executed_plan:Plan, level_stack:LevelStack, name:Optional[str]=None):
        """
        Unlike scenario, you dont need world here, all is in experience level 0 about world understanding of the robot. Scenario is human view for testing
        Args:
            mission:
            executed_plan:
            level_stack: for example level 0 is sensory data, level 1 is clusters
        """
        # initial plan
        self._mission = mission
        self._executed_plan = executed_plan
        self._level_stack = level_stack
        self._name = name

    def get_level_stack(self) -> LevelStack:
        return self._level_stack

    def get_name(self) -> str:
        return self._name

    def get_lowest_level(self)->Level:
        return self._level_stack.get_lowest_level()
