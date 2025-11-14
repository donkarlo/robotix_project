from robotix.mind.memory.composite.component import Component
from robotix.mind.memory.composite.decorator.decorator import Decorator
from robotix.mind.memory.composite.segregation.segregator.segregator import Segregator


class Segregatored(Decorator):
    def __init__(self, inner: Decorator, segregator:Segregator)->None:
        super(Decorator).__init__(self, inner)
        self._segregator = segregator

    def get_segregator(self)->Segregator:
        return self._segregator

    def create_segregated_componnets_as_children(self)->List[Component]:
        segregated_components = self._segregator.get_segregated_components()
        for segregated_component in segregated_components:
            self._inner.add_child(segregated_component)



