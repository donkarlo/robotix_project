from sensorx.sensor_set import SensorSet

from robotix.spa.action.action import Action
from abc import ABC, abstractmethod

from robotix.spa.action.action_set import ActionSet
from robotix.spa.plan.goal.goal import Goal
from robotix.mind.memory.memory import Memory


class Robot(ABC, SensorSet):
    """
    A robot is a sensor set
    """
    def __init__(self, action_set:ActionSet, sensor_set:SensorSet , memory:Memory=None) -> None:
        '''

        Args:
            action_set: Set of commands that are valid for a robot
            sensor_set:
        '''
        self._sensor_set = sensor_set
        self._action_set = action_set
        self._memory = memory

    def build_from_urdf(self, urdf:str):
        """
        URDF to build a robot
        Args:
            urdf:

        Returns:

        """
        pass

    def run_action(self, action:Action):
        self._memory.memorize()


    def achieve_goal(self, goal:Goal) -> None:
        self._memory.memorize()

    @abstractmethod
    def on_action_start(self):
        pass

    @abstractmethod
    def on_action_end(self):
        pass

    @abstractmethod
    def on_goal_achieve_start(self):
        pass

    @abstractmethod
    def on_goal_achieve_end(self):
        pass

    @abstractmethod
    def on_sensor_obs(self):
        pass





