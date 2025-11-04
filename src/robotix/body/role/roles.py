from enum import auto, Enum


class Role(Enum):
    #such as sensors
    receptor = auto()
    # something that can change the state of the world
    manipulator = auto()
    # something that can change the state of the robots
    motor = auto()