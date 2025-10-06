from robotix.mind.language.meaning import Meaning


class Language:
    """For a language first the words are determined then with some methods the necessary alphabets for those words are determined"""
    pass

    def __init__(self, meanings:List[Meaning]):
        self._meanings = meanings

