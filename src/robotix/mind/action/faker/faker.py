from typing import Protocol, runtime_checkable

from robotix.mind.action.action import Action


@runtime_checkable
class Faker(Protocol):
    """
    Is to fake an action
    """
    def fake(self, action:Action) -> Action:
        ...