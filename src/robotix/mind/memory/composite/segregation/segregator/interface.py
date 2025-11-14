from typing import List, Protocol

from robotix.mind.memory.composite.component import Component as MemoryComponent

@runtime_checkable
class Interface(Protocol):
    _source_component:Component
    _segregated_components:List[MemoryComponent]
    def __init__(self, source_component:Component): ...
    def segregate()->None: ...
    def get_segregated_components()->List[MemoryComponent]: ...