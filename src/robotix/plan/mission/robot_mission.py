from robotix.plan.mission.mission import Mission
from robotix.robot import Robot


class RobotMission:
    def __init__(self, robot:Robot, mission:Mission):
        self._robot = robot
        self._mission = mission