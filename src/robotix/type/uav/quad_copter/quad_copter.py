from typing import Optional

from sensorx.sensor_set import SensorSet

from src.robotix.robot import Robot
from robotix.cognition.mind.mind import Mind
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet


class QuadCopter(Robot):
    def __init__(self, rotor_set:RotorSet, sensor_set:SensorSet, mind:Mind, name: Optional[str]=None):
        super().__init__(rotor_set, sensor_set, mind, name)