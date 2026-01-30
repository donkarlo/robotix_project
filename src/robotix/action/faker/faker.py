from typing import Protocol, runtime_checkable

from robotix.action.composite.component import Component


@runtime_checkable
class Faker(Protocol):
    """
    Is to fake an action
    """
    def fake(self, action:Component) -> Component:
        ...