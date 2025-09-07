from typing import Protocol

from robotix.state.state import State


class GoalInterface(Protocol):
    goal_state: State