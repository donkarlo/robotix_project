from robotix.mind.memory.level.level import Level
from typing import List


class LevelStack:
    def __init__(self, levels:List[Level]):
        # sorted from bottom or most basic to to most detailed with more clusters and causality relations
        self._levels = levels

    def add_level(self, level:Level)->None:
        self._levels.append(level)

    def get_levels(self) -> List[Level]:
        return self._levels

    def get_lowest_level(self) -> Level:
        lowest_level = self._levels[0]
        return lowest_level

    def get_highest_level(self) -> Level:
        highest_level = self._levels[-1]
        return highest_level

    def __getitem__(self, index:int)->Level:
        return self._levels[index]