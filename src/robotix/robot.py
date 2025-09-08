from sensorx.sensor_set import SensorSet

from robotix.spa.action.action import Action
from abc import ABC, abstractmethod

from robotix.spa.action.action_set import ActionSet
from robotix.spa.action.actuator.command.command import Command
from robotix.spa.plan.goal.goal import Goal
from robotix.mind.memory.memory import Memory


class Robot(ABC, SensorSet):
    """
    A robot is a sensor set
    """
    def __init__(self, sensor_set:SensorSet , mind) -> None:
        '''

        Args:
            action_set: Set of commands that are valid for a robot
            sensor_set: sich go lef, gi up
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

    @abstractmethod
    def achieve_goal(self, goal:Goal):
        self._check
        pass

    @abstractmethod
    def on_sensor_obs(self):
        pass




