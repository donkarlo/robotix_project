from typing import Optional

from abc import ABC

from robotix.mind.action.composite.plan.plan import Plan
from robotix.mind.goal.composite.mission.mission import Mission
from robotix.robot import Robot
from physix.world.world import World


class Scenario(ABC):
    """
    Scenario is more than a robot and its missions
    """
    def __init__(self, robot:Robot, initial_mission:Mission, initial_plan: Plan, world:World, label:Optional[str]=None):
        """
        
        Args:
            robot: 
            initial_mission: 
            initial_plan: 
            world: 
            label: 
        """
        self._robot = robot
        self._initial_mission = initial_mission
        self._initial_plan = initial_plan

        self._world = world
        self._label = label

        # run

    def run(self)->None:
        self._robot.achieve_mission(self._initial_mission)

    def learn(self):
        self._robot.learn()

    def get_world(self)->World:
        return self._world

    def get_mission(self)->Mission:
        return self._initial_mission

    def get_robot(self)->Robot:
        return self._robot

    def get_plan(self)->Plan:
        return self._initial_plan

    def get_name(self)->str:
        return self._label