from src.robotix.command import Command


class CommandSet:
    def __init__(self, commands:tuple[Command,...]):
        self._commands = commands