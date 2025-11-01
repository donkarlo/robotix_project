from typing import Optional

from sensorx.collection.collection import Collection

from src.robotix.robot import Robot
from robotix.mental.cognition.mind import Mind
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet


class QuadCopter(Robot):
    def __init__(self, rotor_set:RotorSet, sensor_collection:Collection, mind:Mind, name: Optional[str]=None):
        super().__init__(rotor_set, sensor_collection, mind, name)