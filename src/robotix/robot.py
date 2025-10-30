from typing import Optional, List
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.experience import Experience

from sensorx.sensor_set import SensorSet

from robotix.cognition.mind.mind import Mind
from abc import ABC, abstractmethod

from robotix.act.actuator.actuator import Actuator
from robotix.plan.mission.mission import Mission


class Robot(ABC):
    """
    A robot is a sensor set
    """
    def __init__(self, actuators:List[Actuator], sensor_set:SensorSet, mind:Mind, name:Optional[str]=None):
        """

        Args:
            sensor_set:
            mind:
            name:
        """
        self._actuators = actuators
        self._sensor_set = sensor_set
        self._mind:Mind = mind
        self.__name = name

    @abstractmethod
    def achieve_mission(self, mission:Mission)->bool:
        #This is where the robot should remeber
        return False

    @abstractmethod
    def on_sensor_obs(self):
        pass

    @abstractmethod
    def on_mission_change(self):
        pass

    @abstractmethod
    def learn(self)->None:
        self._mind.learn()

    def set_name(self, name:str)->None:
        self.__name = name

    def get_mind(self)->Mind:
        return self._mind

    def get_name(self)->str:
        return self.__name

    def get_experience_by_name(self, name:str)->Experience:
        return self._mind.get_memory().get_experience_collection().get_experience_by_name(name)






