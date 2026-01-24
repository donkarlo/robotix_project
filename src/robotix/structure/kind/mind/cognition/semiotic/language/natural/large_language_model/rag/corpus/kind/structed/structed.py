from abc import ABC, abstractmethod

from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.rag.corpus.corpus import \
    Corpus


class Structed(Corpus, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_plain_text(self)->str:
        pass
