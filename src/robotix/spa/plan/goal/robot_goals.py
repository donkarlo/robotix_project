from robotix.spa.plan.goal.goal import Goal
from robotix.robot import Robot


class RobotGoals:
    def __init__(self, robot:Robot, goals:List[Goal]):
        """
        - TODO: should a robot know about its goals?
        Args:
            robot:
            goals:
        """
        self.__robot = robot
        self.__goals = goals