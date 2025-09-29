from typing import Optional

from sensorx.sensor_set import SensorSet

from robotix.mind.mind import Mind
from abc import ABC, abstractmethod
from robotix.spa.plan.goal.goal import Goal


class Robot(ABC):
    """
    A robot is a sensor set
    """
    def __init__(self, sensor_set:SensorSet , mind:Mind , id:Optional[str]=None) -> None:
        """

        Args:
            sensor_set:
            mind:
            id:
        """
        self._sensor_set = sensor_set
        self._mind:Mind = mind
        self._id = id

    def build_from_urdf(self, urdf:str)->None:
        """
        URDF to build a robot
        Args:
            urdf:

        Returns:

        """
        pass

    @abstractmethod
    def achieve_goal(self, goal:Goal)->bool:
        #This is where the robot should remeber
        return False

    @abstractmethod
    def on_sensor_obs(self):
        pass

    @abstractmethod
    def on_goal_change(self):
        pass

    @abstractmethod
    def learn(self):
        self._mind.learn()




