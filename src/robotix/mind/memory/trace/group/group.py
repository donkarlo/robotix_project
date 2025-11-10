from typing import List, Optional
from robotix.mind.memory.trace.trace import Trace
from robotix.mind.memory.trace.group.interface import Interface
from utilix.data.type.group.group import Group as BaseGroup


class Group(BaseGroup, Interface):
    def __init__(self, traces:Optional[List[Trace]]):
        #just to comply with interface
        super().__init__(traces)

    def get_traces(self) -> Optional[List[Trace]]:
        return self.get_members()