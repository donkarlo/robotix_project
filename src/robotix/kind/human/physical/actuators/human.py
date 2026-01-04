from typing import List, Optional

from robotix.mind.mind import Mind
from robotix.body.actuator.actuator import Actuator
from robotix.robot import Robot
from sensorx.collection.collection import Collection


class Human(Robot):
    """
    This class represts real human and teh actions or messages it can generate
    - a human can convey a message. the robot may or maynot obay
    """
    def __init__(self, actuators: List[Actuator], sensor_collection: Collection, mind: Mind, name: Optional[str] = None):
        pass