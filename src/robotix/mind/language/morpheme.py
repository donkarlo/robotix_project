from robotix.mind.language.meaning import Meaning
from robotix.mind.language.syllable import Syllable


class Morpheme(Meaning):
    """
    Smallest meaningful language component. In persian it is called takvaj
    """
    def __init__(self, syllabels:List[Syllable]):
        self._syllabels = syllabels

    def get_syllables(self)->List[Syllable]:
        return self._syllabels