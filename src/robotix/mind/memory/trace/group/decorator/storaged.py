from typing import List

from robotix.mind.memory.trace.group.decorator.decorator import Decorator
from robotix.mind.memory.trace.group.decorator.interface import Interface
from robotix.mind.memory.trace.trace import Trace
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedStorageInterface



class Storaged(Decorator):
    """
    """
    def __init__(self, inner:Interface,storage: MultiValuedStorageInterface):
        """
        """
        super(Decorator, self).__init__(inner)
        self._storage = storage

    def get_storage(self) -> MultiValuedStorageInterface:
        return self._storage

    def _set_traces(self) -> None:
        ram_values = self._storage.get_ram_values()
        traces = []
        for ram_value in ram_values:
            traces.append(ram_value)
        self._inner._traces = traces

