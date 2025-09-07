from typing import Protocol, runtime_checkable

@runtime_checkable
class HumanControlInterface(Protocol):
    """
    Human control role is to give a new goal to 'Plan'
    """
    pass