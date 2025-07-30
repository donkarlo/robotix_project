from typing import Tuple

from robotix.goal.goal import Goal
from robotix.goal.robot_goal import RobotGoal
from robotix.robot import Robot
class Scenario:
    def __init__(self, robot:Robot, goals:Tuple[Goal,...]):
        self.__robot = robot

    def learn(self)->None:
        pass

    def achieve_goal(self, robot_goal:RobotGoal) -> None:
        pass