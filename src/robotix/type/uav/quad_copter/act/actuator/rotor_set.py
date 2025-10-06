from robotix.act.actuator.actuator_set import ActuatorSet
from robotix.act.actuator.type.rotor.rotor import Rotor
from robotix.type.uav.quad_copter.act.actuator.rotor_position import RotorPosition


class RotorSet(ActuatorSet):
    def __init__(self, rotor:Rotor):
        rotor_class = rotor.__class__
        self._front_left_rotor = rotor_class(RotorPosition.FRONT_LEFT)
        self._front_right_rotor = rotor_class(RotorPosition.FRONT_RIGHT)
        self._rear_left_rotor = rotor_class(RotorPosition.REAR_LEFT)
        self._rear_right_rotor = rotor_class(RotorPosition.REAR_RIGHT)
        super().__init__([self._front_left_rotor, self._front_right_rotor, self._rear_left_rotor, self._rear_right_rotor])

    def get_actuator_set(self) -> ActuatorSet:
        return self._actuator_set
    def get_front_left_rotor(self) -> Rotor:
        return self._front_left_rotor
    def get_front_right_rotor(self) -> Rotor:
        return self._front_right_rotor
    def get_rear_left_rotor(self) -> Rotor:
        return self._rear_left_rotor
    def get_rear_right_rotor(self) -> Rotor:
        return self._rear_right_rotor