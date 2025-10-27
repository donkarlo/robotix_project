from robotix.cognition.mind.language.meaning import Meaning
from robotix.cognition.mind.language.natural.components.syllable import Syllable


class Morpheme(Meaning):
    """
    Smallest meaningful language component. In persian it is called takvaj
    """
    def __init__(self, syllables:List[Syllable]):
        self._syllables = syllables

    def get_syllables(self)->List[Syllable]:
        return self._syllables