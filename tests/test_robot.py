from robotix.robot import Robot
from robotix.structure.kind.body.sensor.kind.group.group import Group
class TestRobot:
    def test__init__(self, sensor_set:Group)->None:
        robot = Robot()