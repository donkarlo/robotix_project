from robotix.robot import Robot
from sensorx.collection.collection import Collection
class TestRobot:
    def test__init__(self, sensor_set:Collection)->None:
        robot = Robot()