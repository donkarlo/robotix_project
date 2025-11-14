from typing import List, Optional
from robotix.mind.memory.trace.trace import Trace
from robotix.mind.memory.trace.group.interface import Interface as GroupInterface
from utilix.data.type.group.group import Group as BaseGroup
from utilix.oop.design_pattern.structural.composite.leaf import Leaf as CompositeLeaf


class Group(BaseGroup, CompositeLeaf, GroupInterface):
    def __init__(self, traces:Optional[List[Trace]], name:Optional[str]):
        #just to comply with interface
        BaseGroup.__init__(self, traces)
        CompositeLeaf.__init__(self, name)

    def get_traces(self) -> Optional[List[Trace]]:
        return self.get_members()