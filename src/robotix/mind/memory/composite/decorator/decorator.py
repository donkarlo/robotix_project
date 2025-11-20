from robotix.mind.memory.composite.component import Component as MemoryComponent
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, MemoryComponent):
    """
    """
    def __init__(self, inner: MemoryComponent):
        BaseDecorator.__init__(self, inner)
