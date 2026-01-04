from typing import List, Optional, Any
from functools import cache

from robotix.trace.group.kind.core.kind import Kind as TraceGoupKind
from robotix.trace.trace import Trace
from robotix.trace.group.interface import Interface as GroupInterface
from utilix.data.kind.group.group import Group as BaseGroup
from utilix.oop.design_pattern.structural.composite.leaf import Leaf as CompositeLeaf


class Group(BaseGroup, CompositeLeaf, GroupInterface):
    def __init__(self, traces:Optional[List[Trace]], name:Optional[str]):
        #just to comply with interface
        BaseGroup.__init__(self, traces)
        CompositeLeaf.__init__(self, name)

        self._kind: Optional[TraceGoupKind] = None

        # lazy loading
        self._formatted_datas = None

    @classmethod
    def init_from_traces_and_kind_and_name(cls, traces: Optional[List[Trace]], kind:Optional[TraceGoupKind],name: Optional[str])->"Group":
        obj = cls(traces, name)
        obj._kind = kind
        return obj

    def get_traces(self) -> Optional[List[Trace]]:
        return self.get_members()

    def get_kind(self)-> TraceGoupKind:
        if self._kind is None:
            self._kind = self.extract_dominant_kind_from_member_trace_kind()
        return self._kind

    def set_name(self, name:str)->None:
        """
        Maybe the name is voted among the mebers of the group
        Args:
            name:

        Returns:

        """
        self._name = name

    def extract_dominant_kind_from_member_trace_kind(self)-> TraceGoupKind:
        ...

    @cache
    def get_formatted_data_list(self)->List[Any]:
        if self._formatted_datas is None:
            self._formatted_datas = []
            for trace in self.get_traces():
                self._formatted_datas.append(trace.get_formatted_data())
            return self._formatted_datas



