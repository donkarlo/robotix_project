from robotix.mind.memory.long_term.explicit.episodic.experience.level.level import Level
from typing import List, Optional

from robotix.mind.memory.long_term.explicit.episodic.experience.level.type.shared_lowest_level import SharedLowestLevel


class Stack:
    shared_lowest_level: SharedLowestLevel
    highest_level: Optional[Level]
    def __init__(self, levels:Optional[List[Level]]=None):
        """
        sorted from bottom or most basic to to most detailed with more clusters and causality relations

        current_level startegy
        - current_level[0] is for raw data such as those for ros messages in topic file, it usually includes _traces without attributing them to any episodes
        - current_level[1] memory>episodic>episodic>collection based: changing representation of data and storing it


        Args:
            levels:
        """
        self._levels = levels if levels is not None else []

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