from sensorx.sensor_set import SensorSet

from robotix.actuator.actuator_set import ActuatorSet
from robotix.action.action import Action
from abc import ABC, abstractmethod

from robotix.action.action_set import ActionSet
from robotix.goal.basic import Basic
from robotix.memory.memory import Memory


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
        self.__sensor_set = sensor_set
        self.__action_set = action_set
        self.__memory = memory

    def build_from_urdf(self, urdf:str):
        """
        URDF to build a robot
        Args:
            urdf:

        Returns:

        """
        pass

    def run_action(self, action:Action):
        self.__memory.memorize()


    def achieve_goal(self, goal:Basic) -> None:
        self.__memory.memorize()

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





