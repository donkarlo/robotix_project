from robotix.cognition.mind.self.awareness.level.level_0 import Level0
from robotix.cognition.mind.self.awareness.level.level_1 import Level0
from robotix.cognition.mind.self.awareness.level.level_2 import Level2
from robotix.cognition.mind.self.awareness.level.level_3 import Level3
from robotix.cognition.mind.self.awareness.level.level_4 import Level4
from robotix.cognition.mind.self.awareness.level.level_5 import Level_5
from typing import List

class Levels:
    def __init__(self):
        self._memebers = List[Level0, Level1, Level2, Level3, Level4, Level_5]

    def get_memebers(self)->List[Level]:
        return self._memebers
