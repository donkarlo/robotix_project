from robotix.mind.memory.composite.component import Component
from utilix.oop.design_pattern.structural.composite.composite import Composite as BaseComposite


class Composite(BaseComposite, Component):
    def __init__(self, name:str):
        super().__init__(name)