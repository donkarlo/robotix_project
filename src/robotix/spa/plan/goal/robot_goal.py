from robotix.spa.plan.goal.goal import Goal
from robotix.robot import Robot


class RobotGoal:
    def __init__(self, robot:Robot, goal:Goal):
        self._robot = robot
        self._goal = goal