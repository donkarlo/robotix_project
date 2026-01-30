from typing import List

from robotix.action.goal.composite.goal import Goal
from robotix.robot import Robot


class RobotMissions:
    def __init__(self, robot:Robot, missions:List[Goal]):
        """
        - TODO: should a robot know about its missions?
        Args:
            robot:
            missions:
        """
        self.__robot = robot
        self.__missions = missions