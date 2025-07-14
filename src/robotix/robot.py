from sensorx.sensor import Sensor
from sensorx.sensor_set import SensorSet

from src.robotix.command import Command


class Robot:
    def __init__(self, sensor_set:SensorSet):
        self._sensor_set = sensor_set

    def run_command(self, command:Command):
        pass
