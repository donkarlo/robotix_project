from robotix.structure.kind.body.sensor.observation.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator


class Decorator(Decorator, Interface):
    def __init__(self, sensor):
        super(Decorator, self).__init__(sensor)