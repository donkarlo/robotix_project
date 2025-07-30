from sensorx.sensor import Sensor
from robotix.robot import Robot


class RobotSensor:
    def __init__(self, robot:Robot, sensor:Sensor):
        self.__robot = robot
        self.__sensor = sensor

