from abc import abstractmethod, ABC
from typing import Tuple

from robotix.world.world import World
from robotix.spa.plan.goal.goal import Goal
from robotix.robot import Robot
class Scenario(ABC):
    """
    Scenario is more than a robot and its goals
    For ecxample it might include the world goal_state such as walls
    """
    def __init__(self, robot:Robot, goal:Goal, world:World):
        """

        :param robot:
        :param goal: Maybe it is a composite and decorated goal, that is a sequence of timed goalsarer
        :param world:
        """
        self._robot = robot
        self._goal = goal
        self._world = world

        # run

    def run(self)->None:
        self._robot.achieve_goal(self._goal)

    def learn(self):
        self._robot.learn()

    def get_world(self)->World:
        return self._world

    def get_goal(self)->Goal:
        return self._goal

    def get_robot(self)->Robot:
        return self._robot