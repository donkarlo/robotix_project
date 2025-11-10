from typing import List
from robotix.mind.memory.trace.group.decorator.decorator import Decorator
from robotix.mind.memory.trace.group.interface import Interface
from robotix.mind.memory.trace.population_filled import PopulationFilled
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedStorageInterface



class Storaged(Decorator):
    """
    """
    def __init__(self, inner:Interface, storage: MultiValuedStorageInterface):
        """
        """
        super(Decorator, self).__init__(inner)
        self._storage = storage

    def get_storage(self) -> MultiValuedStorageInterface:
        return self._storage

    def get_members(self, slc:slice)->List[PopulationFilled]:
        if slc is not None:
            members = self._storage.get_ram_values_from_values_slices_by_slice(slc)
        else:
            members = self._storage.get_ram_values()
        self._inner.reset_members(members)
        return super().get_members()