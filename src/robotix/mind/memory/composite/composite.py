from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from utilix.oop.design_pattern.structural.composite.composite import Composite as BaseComposite


class Composite(MemoryComponent, BaseComposite):
    def __init__(self, trace_group:TraceGroup | None, name:str):
        """

        Args:
            trace_group: can be None to only host the link (child) to the next leaf (trace group here) or composite (only link/child or a trace group)
            name:
        """
        MemoryComponent.__init__(self, trace_group, name)
        BaseComposite.__init__(self, name)

