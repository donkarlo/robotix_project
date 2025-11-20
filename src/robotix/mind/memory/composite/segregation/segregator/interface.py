from typing import List, Protocol, runtime_checkable

from robotix.mind.memory.composite.component import Component as MemoryComponent

@runtime_checkable
class Interface(Protocol):
    _source_component: MemoryComponent
    _segregated_components:List[MemoryComponent]
    def __init__(self, source_component: MemoryComponent): ...
    def segregate()->None: ...
    def get_segregated_components()->List[MemoryComponent]: ...