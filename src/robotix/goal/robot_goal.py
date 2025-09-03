from robotix.goal.basic import Basic
from robotix.robot import Robot


class RobotGoal:
    def __init__(self, robot:Robot, goal:Basic):
        self._robot = robot
        self._goal = goal