from robotix.goal.goal import Goal
from robotix.robot import Robot


class RobotGoal:
    def __init__(self, robot:Robot, goal:Goal):
        self.__robot = robot
        self.__goal = goal