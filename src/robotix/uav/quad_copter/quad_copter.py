from sensorx.sensor_set import SensorSet

from src.robotix.robot import Robot


class QuadCopter(Robot):
    def __init__(self, sensor_set:SensorSet):
        super().__init__(sensor_set)