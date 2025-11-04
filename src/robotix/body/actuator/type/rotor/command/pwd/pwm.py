from robotix.body.actuator.command.command import Command
from physix.dimension.unit.scalar import Scalar


class Pwm(Command):
    def __init__(self, time:Scalar=0):
        """

        Args:
            time: is usually in microseconds
        """
        self._time = time
        super().__init__()

    def get_time(self):
        return self._time