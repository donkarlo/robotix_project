from abc import abstractmethod

from sensorx.sensor_set import SensorSet

from robotix.goal.basic import Basic
class Remembering:
    """
    This class abstracts a strategy for remebering
    The action of remebering by an evidence, episode or sequence of observation or just will
    - remembering is the process of bringing (meaningful) data from long-term memory
    """
    def __init__(self, provoker:Provoker):
        """It is not necessary to set the data source as it is already introduced in Memorizing class and Remebering and Memorizing class are bounded in Memory class"""
        pass

    @abstractmethod
    def remember(self, goal:Basic, sensor_set:SensorSet)->Provoker:
        pass

    def load(self):
        pass