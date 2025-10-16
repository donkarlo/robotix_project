from typing import Optional

from abc import ABC

from robotix.plan.plan import Plan
from robotix.plan.mission.mission import Mission
from robotix.robot import Robot
from physix.world.world import World


class Scenario(ABC):
    """
    Scenario is more than a robot and its missions
    For ecxample it might include the world mission_state such as walls
    """
    def __init__(self, robot:Robot, mission:Mission, plan: Plan, world:World, name:Optional[str]=None):
        """

        :param robot:
        :param mission: Maybe it is a composite and decorated mission, that is a sequence of timed missionsarer
        :param world:
        """
        self._robot = robot
        self._mission = mission
        self._plan = plan

        self._world = world
        self._name = name

        # run

    def run(self)->None:
        self._robot.achieve_mission(self._mission)

    def learn(self):
        self._robot.learn()

    def get_world(self)->World:
        return self._world

    def get_mission(self)->Mission:
        return self._mission

    def get_robot(self)->Robot:
        return self._robot

    def get_plan(self)->Plan:
        return self._plan

    def get_name(self)->str:
        return self._name