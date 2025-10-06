from robotix.robot import Robot
from typing import List, Optional
from robotix.act.actuator.actuator_set import ActuatorSet
from sensorx.sensor_set import SensorSet
from robotix.mind.mind import Mind
import copy

class Factory:
    def __init__(self, sample_robot:Robot):
        """

        Args:
            actuator_set:
            sensor_set:
            mind:
        """
        self._sample_robot = sample_robot
        self._robots:List[Robot] = []

    def add_robots(self, ids: Optional[List[str]]=None)->None:
        """

        Args:
            ids:

        Returns:

        """
        for counter, id in enumerate(ids):
            # TODO: check uniqness of the id
            copied_robot = copy.deepcopy(self._sample_robot)
            copied_robot.set_id(id)
            self._robots.append(copied_robot)

    def get_robots(self)->List[Robot]:
        return self._robots

