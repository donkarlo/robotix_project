from typing import Optional

from robotix.structure.kind.body.sensor.kind.group.group import Group

from src.robotix.robot import Robot
from robotix.structure.kind.mind.mind import Mind
from robotix.kind.uav.quad_copter.act.actuator.rotor_set import RotorSet


class QuadCopter(Robot):
    def __init__(self, rotor_set:RotorSet, sensor_collection:Group, mind:Mind, name: Optional[str]=None):
        super().__init__(rotor_set, sensor_collection, mind, name)