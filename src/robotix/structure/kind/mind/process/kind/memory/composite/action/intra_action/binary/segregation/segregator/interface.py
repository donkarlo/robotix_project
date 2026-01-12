from typing import List, Protocol, runtime_checkable, Optional

from robotix.structure.kind.mind.process.kind.memory.composite.component import Component as MemoryComponent

@runtime_checkable
class Interface(Protocol):
    _source_memory_component: MemoryComponent
    _segregated_components:Optional[List[MemoryComponent]]

    def __init__(self, source_memory_component: MemoryComponent):
        ...
    def segregate(self)->None:
        ...
    def get_segregated_components(self)->List[MemoryComponent]:
        ...