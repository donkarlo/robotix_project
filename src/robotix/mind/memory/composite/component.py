from abc import abstractmethod

from robotix.mind.memory.trace.group.group import Group as TraceGroup
from utilix.oop.design_pattern.structural.composite.component import Component as BaseComponent


class Component(BaseComponent):
    def __init__(self, trace_group: TraceGroup, name:str):
        super().__init__(name)
        self._trace_group = trace_group

    def get_trace_group(self)-> TraceGroup:
        return self._trace_group