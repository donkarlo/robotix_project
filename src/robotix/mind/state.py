from enum import auto, Enum


class State(Enum):
    DOING = auto()
    REMEMBERING = auto()
    BEING_CONTROLLED = auto()
    BEING_AUTONOMOUS = auto()

    def __init__(self, state: int):
        self._state = state
    def get_state(self)->int:
        return self._state