from robotix.mind.ontology.message.interface import Interface as MessageInterface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as DesignPatternsDecorator


class Decorator(MessageInterface, DesignPatternsDecorator):
    def __init__(self, inner: StorageInterface):
        self._inner = inner