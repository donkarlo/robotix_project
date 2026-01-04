from robotix.mind.cognition.process.kind.memory.composite.composite import Composite as MemoryComposite
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(MemoryComposite, BaseDecorator):
    def __init__(self, inner: MemoryComposite):
        MemoryComposite.__init__(self, inner.get_trace_group(), inner.get_name())
        BaseDecorator.__init__(self, inner)
