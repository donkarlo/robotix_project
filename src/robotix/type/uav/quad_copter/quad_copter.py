from sensorx.sensor_set import SensorSet

from robotix.spa.action.actuator.actuator_set import ActuatorSet
from src.robotix.robot import Robot


class QuadCopter(Robot):
    def __init__(self, actuator_set:ActuatorSet, sensor_set:SensorSet):
        super().__init__(sensor_set)