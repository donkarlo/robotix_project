from robotix.act.actuator.command.command import Command
from robotix.act.actuator.type.rotor.command.pwd.pwm import Pwm
from robotix.act.actuator.actuator import Actuator
from robotix.act.actuator.type.rotor.command.arm.status import Status as ArmStatus
from robotix.act.actuator.type.rotor.command.arm.arm import Arm
from robotix.act.actuator.type.rotor.command.direction.status import Status as DirectionStatus
from robotix.act.actuator.type.rotor.command.direction.direction import Direction
from typing import Optional

class Rotor(Actuator):
    def __init__(self, id:Optional[str]=None):
        arm_command = Arm(ArmStatus.DISARMED)
        direction_command = Direction(DirectionStatus.CW)
        pwm_command = Pwm()
        valid_commands = [arm_command, direction_command, pwm_command]
        super().__init__(valid_commands, id)

    def _do_run_command(self, command:Command):
       if isinstance(command, Arm):
           pass
       elif isinstance(command, Direction):
           pass
       elif isinstance(command, Pwm):
           pass


