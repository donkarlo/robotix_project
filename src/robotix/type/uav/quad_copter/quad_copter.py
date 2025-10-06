from robotix.type.uav.quad_copter.act.actuator.rotor_position import RotorPosition
from typing import Optional

from sensorx.sensor_set import SensorSet

from robotix.act.actuator.actuator_set import ActuatorSet
from robotix.act.actuator.type.rotor.rotor import Rotor
from src.robotix.robot import Robot
from robotix.mind.mind import Mind
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet


class QuadCopter(Robot):
    def __init__(self, rotor_set:RotorSet, sensor_set:SensorSet, mind:Mind, id: Optional[str]=None):
        super().__init__(rotor_set, sensor_set, mind, id)