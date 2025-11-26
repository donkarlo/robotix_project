from typing import List, Any, Optional

from overrides import overrides
from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.group.decorator.decorator import Decorator as TraceGroupDecorator
from robotix.mind.memory.trace.group.interface import Interface as TraceGroupInterface
from utilix.data.storage.decorator.multi_valued.slices_cashed_interface import SlicesCashedInterface as MultiValuedStorageInterface
from utilix.data.storage.interface import Interface as StorageInterface


class Storaged(TraceGroupDecorator, StorageInterface):
    """
    """
    def __init__(self, inner:TraceGroup, storage: MultiValuedStorageInterface):
        """
        """
        TraceGroupDecorator.__init__(self, inner)
        self._storage = storage
        tgm = inner.get_members()
        self._storage.set_ram(inner.get_members())

    def get_storage(self) -> MultiValuedStorageInterface:
        return self._storage

    def save(self)->None:
        self._storage.save()

    def load(self)->None:
        self._storage.load()
