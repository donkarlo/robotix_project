from abc import ABC, abstractmethod

from robotix.body.actuator.collection.collection import Collection as ActuatorCollection
from robotix.mind.goal.goal import Goal

class Action(ABC):
    """
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running missions. They consist of three parts: a role, feedback, and a result.
    - Action is assessable
    - It is also an abstraction. what we call a verb in NLP
    - MAVLINK defines actions
    - if an role is breakable to smaller actions then it is actually a Mission
    - History will be kept in episodes
    - TODO
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