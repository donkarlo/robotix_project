from robotix.mind.consciousness.awareness.self.awareness import Level0
from robotix.mind.consciousness.awareness.self.awareness import Level0
from robotix.mind.consciousness.awareness.self.awareness import Level2
from robotix.mind.consciousness.awareness.self.awareness import Level3
from robotix.mind.consciousness.awareness.self.awareness import Level4
from robotix.mind.consciousness.awareness.self.awareness import Level_5
from typing import List

class Levels:
    def __init__(self):
        self._memebers = List[Level0, Level1, Level2, Level3, Level4, Level_5]

    def get_memebers(self)->List[Level]:
        return self._memebers
