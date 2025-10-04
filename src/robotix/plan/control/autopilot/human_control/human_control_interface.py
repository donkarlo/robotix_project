from typing import Protocol, runtime_checkable

@runtime_checkable
class HumanControlInterface(Protocol):
    """
    Human control role is to give a new mission to 'Plan'
    """
    pass