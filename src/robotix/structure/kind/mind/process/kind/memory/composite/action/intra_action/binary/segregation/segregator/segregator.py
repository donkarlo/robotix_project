from typing import List, Optional
from robotix.structure.kind.mind.process.kind.memory.composite.component import Component as MemoryComponent
from robotix.structure.kind.mind.process.kind.memory.composite.action.intra_action.binary.segregation.segregator.interface import Interface as SegregatorInterface
from abc import ABC, abstractmethod


class Segregator(SegregatorInterface, ABC):
    """
    Neurological term for seprating different senses that we use here for a trace group to seprate it should cover
    - Segregation is an effort to reduce suprise
    - separating modalities
    - clustering

    """
    def __init__(self, source_memory_component:MemoryComponent):
        self._source_memory_component = source_memory_component

        # cached
        self._segregated_components:Optional[List[MemoryComponent]] = None

    def get_segregated_components(self)->List[MemoryComponent]:
        if self._segregated_components is None:
            self._segregated_components = []
            self.segregate()
        return self._segregated_components

    @abstractmethod
    def segregate(self)->None: ...

