from typing import List

from robotix.mind.memory.long_term.modality.modality import Modality
from robotix.mind.memory.stack.stack import Stack
from utilix.data.type.group.single_type import SingleType as BaseGroup


class Group(BaseGroup[Modality]):
    """
    Each experience will have a group of modalities
    """
    def __init__(self, members:List[Modality], shared_stack:Stack):
        super().__init__(members)
        self._shared_stack = shared_stack
    def get_shared_stack(self) -> Stack:
        return self._shared_stack