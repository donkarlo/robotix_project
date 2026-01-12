from robotix.structure.kind.body.actuator.command.command import Command
from robotix.structure.kind.body.actuator.kind.rotor.command.direction.status import Status


class Direction(Command):
    def __init__(self, status:Status):
        self._status = status
        super().__init__()