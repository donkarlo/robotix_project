from sensorx.sensor_set import SensorSet

from robotix.actuator.actuator_set import ActuatorSet
from robotix.action.action import Action
from abc import ABC, abstractmethod

from robotix.action.action_set import ActionSet
from robotix.goal.goal import Goal


class Robot(ABC):
    def __init__(self, action_set:ActionSet, actuator_set:ActuatorSet, sensor_set:SensorSet):
        '''

        Args:
            action_set: Set of commands that are valid for a robot
            actuator_set:
            sensor_set:
        '''
        self._sensor_set = sensor_set
        self._actuator_set = actuator_set
        self._action_set = action_set

    @abstractmethod
    def run_command(self, cmd:Action):
        pass

    @abstractmethod
    def achieve_goal(self, goal:Goal, sensor_set_to_record:SensorSet|bool|None=None) -> None:
        record = True
        if sensor_set_to_record == None:
            record = False
        if sensor_set_to_record == True:
            sensor_set_to_record = None

