from robotix.type.uav.quad_copter.actuator.rotor_position import RotorPosition
from typing import Optional

from sensorx.sensor_set import SensorSet

from robotix.act.actuator.actuator_set import ActuatorSet
from robotix.act.actuator.type.rotor.rotor import Rotor
from src.robotix.robot import Robot
from robotix.mind.mind import Mind


class QuadCopter(Robot):
    def __init__(self, sensor_set:SensorSet, mind:Mind , model_id:Optional[str]=None):
        front_left_rotor = Rotor(RotorPosition.FRONT_LEFT)
        front_right_rotor = Rotor(RotorPosition.FRONT_RIGHT)
        rear_left_rotor = Rotor(RotorPosition.REAR_LEFT)
        rear_right_rotor = Rotor(RotorPosition.REAR_RIGHT)

        actuator_set = ActuatorSet([front_left_rotor, front_right_rotor, rear_left_rotor, rear_right_rotor])
        super().__init__(actuator_set, sensor_set, mind)