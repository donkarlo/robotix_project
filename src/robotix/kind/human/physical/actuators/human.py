from typing import List, Optional

from robotix.structure.kind.mind.mind import Mind
from robotix.structure.kind.body.actuator.actuator import Actuator
from robotix.robot import Robot
from robotix.structure.kind.body.sensor.kind.group.group import Group


class Human(Robot):
    """
    This class represts real human and teh actions or messages it can generate
    - a human can convey a message. the robot may or maynot obay
    """
    def __init__(self, actuators: List[Actuator], sensor_collection: Group, mind: Mind, name: Optional[str] = None):
        pass