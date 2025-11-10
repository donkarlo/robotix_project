from typing import Optional, Union
from robotix.mind.memory.long_term.explicit.episodic.experience.experience import Experience
from robotix.body.body import Body
from robotix.mind.memory.force import Force
from robotix.mind.mind import Mind
from abc import ABC


class Robot(ABC):
    """
    A robot is a sensor set
    """
    def __init__(self, body:Body, mind:Mind, name:Optional[str]=None):
        """
        Todo: integrate sensors and actuators in to body part and change mind by mind
        Args:
            actuators: An actuator might also be used for comunicating with the world
            sensor_collection: for observing the world
            mind:
            name: meaningful only in a group. It is given the first time by the group and remebered and probably used and conveyed by the target robot while attending later groups
        """
        self._body = body
        self._mind:Mind = mind
        self.__name = name

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

    def remember_experience_by_name(self, name:str)->Experience:
        return self._mind.get_memory().get_experience_group().get_experience_by_name(name)

    def remember(self, trigger:Optional[Force]=None)->Union[Experience]:
        print("I am remebering")
        return self._mind.get_memory().get_remembering().remember(trigger)






