from typing import List
from robotix.mind.memory.composite.component import Component as MemoryComponent
from abc import ABC, abstractmethod


class Segregator(ABC, Interface):
    """
    Neurological term for seprating different senses that we use here for a trace group to seprate it should cover
    - separating modalities
    - clustering
    """
    def __init__(self, source_component:MemoryComponent):
        self._source_component = source_component

        # cached
        self._segregated_components:List[MemoryComponent] = []

    def get_segregated_components(self)->List[MemoryComponent]:
        if self._segregated_components == []:
            self.segregate()
        return self._segregated_components

    @abstractmethod
    def segregate(self)->None: ...

