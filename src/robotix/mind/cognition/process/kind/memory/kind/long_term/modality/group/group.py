from typing import List

from robotix.mind.cognition.process.kind.memory.kind.long_term.modality.modality import Modality
from utilix.data.kind.group.group import Group as BaseGroup


class Group(BaseGroup):
    """
    Each experience will have a group of modalities
    """
    def __init__(self, members:List[Modality]):
        super().__init__(members)