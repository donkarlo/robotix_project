from robotix.mind.memory.long_term.explicit.experience.modality.stack.layer.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(BaseDecorator, Interface):
    def __init__(self, inner:Interface):
        super().__init__(inner)