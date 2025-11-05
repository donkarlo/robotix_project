from typing import List

from robotix.mind.memory.long_term.explicit.experience.modality.modality import Modality
from utilix.data.type.collection.single_type_collection import SingleTypeCollection as BaseCollection


class Collection(BaseCollection[Modality]):
    """
    Each experience will have a collection of modalities
    """
    def __init__(self, modality_members:List[Modality]):
        self._members = modality_members