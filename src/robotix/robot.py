from sensorx.sensor_set import SensorSet
from robotix.cmd.cmd import Cmd


class Robot:
    def __init__(self, sensor_set:SensorSet):
        self._sensor_set = sensor_set

    def run_command(self, cmd:Cmd):
        pass
