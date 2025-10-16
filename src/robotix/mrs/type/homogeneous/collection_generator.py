from robotix.robot import Robot
from typing import List, Optional
from robotix.act.actuator.actuator_set import ActuatorSet
from sensorx.sensor_set import SensorSet
from robotix.mind.mind import Mind
import copy

class CollectionGenerator:

    @staticmethod
    def get_robots_by_sample(sample_robot: Robot, names: List[str]=None)->List[Robot]:
        """

        Args:
            names:

        Returns:

        """
        for counter, name in enumerate(names):
            # TODO: check uniqness of the name
            copied_robot = copy.deepcopy(sample_robot)
            copied_robot.set_name(name)
            robots.append(copied_robot)
        return robots

