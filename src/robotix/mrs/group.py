from abc import abstractmethod, ABC
from typing import List

from robotix.spa.plan.goal.goal import Goal
from src.robotix.robot import Robot


class Group(ABC):
    '''A set of robots whose states are inter related through commands'''
    def __init__(self, robot_members:List[Robot]):
        self._members = robot_members

    def add_robot(self, robot:Robot)->None:
        # TODO: check for uniquness
        self._members.append(robot)

    def get_members(self)->List[Robot]:
        return self._members

    def achieve_goal(self, robot:Robot, goal:Goal)->bool:
        return robot.achieve_goal(goal)