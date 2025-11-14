from typing import List, Any, Optional

from overrides import overrides
from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.group.decorator.decorator import Decorator as TraceGroupDecorator
from robotix.mind.memory.trace.group.interface import Interface as TraceGroupInterface


class Storaged(TraceGroupDecorator):
    """
    """
    def __init__(self, inner: TraceGroup, storage: MultiValuedStorageInterface):
        """
        """
        Decorator.__init__(self, inner)
        self._storage = storage

    def get_storage(self) -> MultiValuedStorageInterface:
        return self._storage