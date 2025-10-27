from typing import List

from robotix.platform.ros.message.interface import Interface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator


class Decorator(Interface, BaseDecorator):
    def __init__(self, inner:Interface):
        super(Decorator, self).__init__(inner)

    def get_fields(self) -> List[Field]:
        return self._inner.get_fields()