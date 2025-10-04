from robotix.act.actuator.command.command import Command
from robotix.act.actuator.type.rotor.command.arm.status import Status


class Arm(Command):
    def __init__(self, status: Status):
        self._status = status
        super().__init__()

    def get_status(self) -> Status:
        return self._status