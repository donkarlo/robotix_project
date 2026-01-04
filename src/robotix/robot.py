from typing import Optional, Union
from robotix.mind.cognition.process.kind.memory.kind.long_term.explicit.episodic.experience.experience import Experience
from robotix.body.body import Body
from robotix.mind.cognition.process.kind.memory.force import Force
from robotix.mind.mind import Mind
from abc import ABC



class Robot(ABC):
    """
    A robot is a sensor set
    """
    def __init__(self, body:Body, mind:Mind, name:Optional[str]):
        """

        Args:
            body: includes brain to
            mind: where activity potential fields are converted to meaningful values
            name:
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
        return self._mind.get_memory().get_memory_tree().get_experience_by_name(name)

    def remember(self, trigger:Optional[Force]=None)->Union[Experience]:
        print("I am remebering")
        return self._mind.get_memory().get_remembering().remember(trigger)

    def wake_up(self)->None:
        # loading memories
        # if self._mind.get_memory().get
        pass







