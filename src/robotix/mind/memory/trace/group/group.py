from typing import List, overload, Union
from robotix.mind.memory.trace.trace import Trace
from utilix.data.storage.storage import Storage
from utilix.data.type.group.group import Group as BaseGroup


class Group(BaseGroup):
    def __init__(self, traces:List[Trace]):
        super().__init__(traces)
    def get_traces(self) -> List[Trace]:
        return self.get_members()