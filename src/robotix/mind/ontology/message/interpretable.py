from robotix.robot import Robot
from typing import Protocol, Any

class interpretable(Protocol):
    def get_interpretion(self, interpreter:Robot)->Any: ...
