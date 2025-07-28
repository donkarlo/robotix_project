from sensorx.sensor_set import SensorSet
from robotix.cmd.cmd import Cmd
from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, actuator_set:ActuatorSet, sensor_set:SensorSet):
        self._sensor_set = sensor_set

    @abstractmethod
    def run_cmd(self, cmd:Cmd):
        pass
