from robotix.structure.kind.mind.action.goal.composite.goal import Goal
from robotix.robot import Robot


class RobotMission:
    def __init__(self, robot:Robot, mission:Goal):
        self._robot = robot
        self._mission = mission