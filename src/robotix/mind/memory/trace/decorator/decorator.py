from robotix.mind.memory.trace.interface import Interface as TraceInterface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, TraceInterface):
    """
    """

    def __init__(self, inner:TraceInterface):
        BaseDecorator.__init__(self, inner)


