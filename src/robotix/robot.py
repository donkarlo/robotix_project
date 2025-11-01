from typing import Optional, List, Union
from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.experience import Experience
from robotix.physical.sensor.new_sensor_observation_observer import NewSensorObservationObserver

from sensorx.collection.collection import Collection as SensorCollection

from robotix.mental.cognition.memory.trigger import Trigger
from robotix.mental.cognition.mind import Mind
from abc import ABC, abstractmethod

from robotix.physical.actuator.actuator import Actuator
from robotix.plan.mission.mission import Mission


class Robot(ABC, NewSensorObservationObserver):
    """
    A robot is a sensor set
    """
    def __init__(self, actuators:List[Actuator], sensor_collection: SensorCollection, mind:Mind, name:Optional[str]=None):
        """
        Todo: integrate sensors and actuators in to physical part and change mind by mental
        Args:
            actuators: An actuator might also be used for comunicating with the world
            sensor_collection: for observing the world
            mind:
            name: meaningful only in a group. It is given the first time by the group and remebered and probably used and conveyed by the target robot while attending later groups
        """
        self._actuators = actuators
        self._sensor_collection = sensor_collection
        self._mind:Mind = mind
        self.__name = name

        #
        senosr_new_observation_observers:List[]

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

    def learn(self)->None:
        pass

    def set_name(self, name:str)->None:
        """
        usualled called ina population of robots
        Args:
            name:

        Returns:

        """
        self.__name = name

    def get_mind(self)->Mind:
        return self._mind

    def get_name(self)->Optional[str]:
        return self.__name

    def get_experience_by_name(self, name:str)->Experience:
        return self._mind.get_memory().get_experience_collection().get_experience_by_name(name)

    def remember(self, trigger:Optional[Trigger]=None)->Union[Experience]:
        return self._mind.get_memory().get_remembering().remember(trigger)

    def attach_senosr_new_observation_observer(self, senosr_new_observation_observer)->None:
        pass






