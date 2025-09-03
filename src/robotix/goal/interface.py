from typing import Protocol

from robotix.state.state import State


class Interface(Protocol):
    state: State