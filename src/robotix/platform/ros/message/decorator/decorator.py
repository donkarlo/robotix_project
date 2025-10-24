from robotix.platform.ros.message.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator


class Decorator(Interface, Decorator):
    def __init__(self, inner:Interface):
        super(Decorator, self).__init__(inner)