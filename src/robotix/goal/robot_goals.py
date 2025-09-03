from typing import Tuple
from robotix.goal.basic import Basic
from robotix.robot import Robot


class RobotGoals:
    def __init__(self, robot:Robot, goals:List[Basic]):
        """
        - TODO: should a robot know about its goals?
        Args:
            robot:
            goals:
        """
        self.__robot = robot
        self.__goals = goals