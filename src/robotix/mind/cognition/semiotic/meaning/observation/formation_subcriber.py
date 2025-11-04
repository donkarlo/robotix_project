from typing import Protocol

from robotix.mind.cognition.semiotic.meaning.meaning import Meaning


class FormationSubscriber(Protocol):
    def do_with_formed_meaning(self, meaning:Meaning) -> Meaning: ...