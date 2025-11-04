from typing import List

from robotix.mind.goal.composite.mission.mission import Mission
from robotix.robot import Robot


class RobotMissions:
    def __init__(self, robot:Robot, missions:List[Mission]):
        """
        - TODO: should a robot know about its missions?
        Args:
            robot:
            missions:
        """
        self.__robot = robot
        self.__missions = missions