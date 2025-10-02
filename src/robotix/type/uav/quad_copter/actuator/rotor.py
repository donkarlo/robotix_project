from robotix.spa.action.actuator.actuator import Actuator
from robotix.type.uav.quad_copter.actuator.rotor_position import RotorPosition


class Rotor(Actuator):
    def __init__(self, position: RotorPosition):
        self._rotation_speed = 0.0
        self.__rotor_position = position

    def set_rotation_speed(self, rotation_speed:float)->None:
        self._rotation_speed = rotation_speed

    def stop(self)->None:
        self.set_rotation_speed(0.0)