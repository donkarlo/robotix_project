from abc import ABC, abstractmethod

from robotix.structure.kind.body.actuator.group.collection import Collection as ActuatorCollection
from robotix.action.goal.goal import Goal
from utilix.oop.design_pattern.structural.composite.component import Component as BaseComponent


class Component(BaseComponent, ABC):
    """
    - It is an action
    - Goal in this package is something that takes the robot , either mentally or physically from one state to another state whic is a goal state.
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running missions. They consist of three parts: a role, feedback, and a result.
    - Goal is assessable
    - It is also an abstraction. what we call a verb in NLP
    - MAVLINK defines actions
    - if an role is breakable to smaller actions then it is actually a Goal
    - History will be kept in episodes
    """
    def __init__(self, goal:Goal, involving_actuators: ActuatorCollection):
        self._goal = goal
        self._involving_actuators = involving_actuators

    def get_goal(self)->Goal:
        return self._goal

    def get_involving_actuators(self)->ActuatorCollection:
        return self._involving_actuators

    @abstractmethod
    def run(self):
        pass