from sensorx.state.state import State
from robotix.robot import Robot


class RobotState:
    def __init__(self, robot:Robot, state:State):
        self.__robot = robot
        self.__state = state