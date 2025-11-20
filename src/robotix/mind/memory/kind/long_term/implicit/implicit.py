from robotix.mind.memory.kind.long_term.implicit.conditioned.conditioned import Conditioned
from robotix.mind.memory.kind.long_term.implicit.habitual.habitual import Habitual
from robotix.mind.memory.kind.long_term.implicit.priming.priming import Priming
from robotix.mind.memory.kind.long_term.implicit.procedural.procedural import Procedural


class Implicit:
    def __init__(self):
        """
        loading by order that human brain loads
        """
        self._procedural = Procedural()
        self._priming = Priming()
        self._conditioned = Conditioned()
        self._habitual = Habitual()