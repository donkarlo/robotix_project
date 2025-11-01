from typing import List

from robotix.mental.cognition.language.natural.phoneme import Phoneme


class Syllable:
    def __init__(self, phonems:List[Phoneme]):
        self._phonems = phonems
    def get_phonems(self)->List[Phoneme]:
        return self._phonems