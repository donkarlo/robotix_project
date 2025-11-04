from robotix.mind.memory.long_term.explicit.episodic.experience.level.decorator.decorator import Decorator
from typing import List

class Clustered(Decorator):
    def __init__(self, inner:Decorator, clusters:List):
        super().__init__(inner)
        self._clusters = clusters