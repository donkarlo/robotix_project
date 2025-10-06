from robotix.mind.memory.level.level import Level
from typing import List


class Levels:
    def __init__(self, members:List[Level]):
        self._members = members

    def add_level(self, level:Level)->None:
        self._members.append(level)