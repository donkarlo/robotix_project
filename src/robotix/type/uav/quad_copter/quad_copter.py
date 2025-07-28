from robotix.type.uav.quad_copter.cmd import Cmd as QuadCopterCmd
from sensorx.sensor_set import SensorSet

from src.robotix.robot import Robot


class QuadCopter(Robot):
    def __init__(self, actuator_set:ActuatorSet, sensor_set:SensorSet):
        super().__init__(sensor_set)

    def run_cmd(self, cmd:QuadCopterCmd):
        if isinstance(cmd, QuadCopterCmd):
            cmd.run()