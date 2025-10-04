from robotix.act.actuator.command.command import Command
from robotix.act.actuator.type.rotor.command.direction.status import Status


class Direction(Command):
    def __init__(self, status:Status):
        self._status = status
        super().__init__()