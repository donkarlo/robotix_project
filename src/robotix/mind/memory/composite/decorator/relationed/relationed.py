from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.composite.decorator.decorator import Decorator
from robotix.mind.memory.composite.decorator.relationed.relations import Relations


class Relationed(Decorator):
    def __init__(self, inner: MemoryComponent, relationes:Relations):
        self._relations = relationes

    def get_relations(self)->Relations:
        return self._relations