from typing import List

from robotix.mind.memory.long_term.modality.modality import Modality
from utilix.data.type.group.group import Group as BaseGroup


class Group(BaseGroup):
    """
    Each experience will have a group of modalities
    """
    def __init__(self, members:List[Modality]):
        super().__init__(members)