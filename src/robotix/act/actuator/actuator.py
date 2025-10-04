from robotix.act.actuator.command.command import Command
from abc import abstractmethod, ABC

class Actuator(ABC):
    def __init__(self, valid_commands:tuple[Command], id:str=None):
        self._valid_commands = valid_commands
        self._id = id

    def run_command(self, command:Command)->None:
        if command not in self._valid_commands:
            raise ValueError("Invalid command")
        self._do_run_command()

    @abstractmethod
    def _do_run_command(self):
        pass
