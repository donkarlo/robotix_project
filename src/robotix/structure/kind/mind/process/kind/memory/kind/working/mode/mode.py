from typing import List

from robotix.mind.cognition.process.kind.memory.mode.kind.core.kind import Kind


class Mode:
    """
    - multiple states at once are possible
    """

    def __init__(self, current_modes: List[Kind]):
        self._current_modes = current_modes

    def get_current_states(self) -> List[int]:
        return self._current_modes

    def has_mode(self, state: Kind) -> bool:
        if state in self._current_modes:
            return True
        return False