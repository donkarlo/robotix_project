from robotix.mental.cognition.language.meaning import Meaning
from robotix.mental.cognition.language.natural.components.syllable import Syllable


class Morpheme(Meaning):
    """
    Smallest meaningful language component. In persian it is called takvaj
    """
    def __init__(self, syllables:List[Syllable]):
        self._syllables = syllables

    def get_syllables(self)->List[Syllable]:
        return self._syllables

    def get_probable_next_plan_by_morphem(self)->Plan:
        pass