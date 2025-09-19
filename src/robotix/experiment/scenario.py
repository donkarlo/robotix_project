from abc import abstractmethod, ABC
from typing import Tuple

from robotix.environment.environment import Environment
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



    def run(self)->None:
        for goal in self._goal:
            self._robot.achieve_goal(goal)

    def learn(self)->None:
        learning_data = None
        if learning_data:
            self.run()


    @abstractmethod
    def do_learn(self)->None:
        pass