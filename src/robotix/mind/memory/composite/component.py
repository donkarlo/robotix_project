from abc import abstractmethod

from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.trace import Trace
from utilix.oop.design_pattern.structural.composite.component import Component as BaseComponent
from utilix.os.file_system.path.path import Path


class Component(BaseComponent):
    """
    The component, either leaf or composite can only have one trace_group
    """
    def __init__(self, trace_group:TraceGroup, name:str):
        super().__init__(name)
        self._trace_group = trace_group

    def get_trace_group(self)-> TraceGroup:
        return self._trace_group

    def add_trace(self, trace:Trace)->None:
        self._trace_group.add_member(trace)