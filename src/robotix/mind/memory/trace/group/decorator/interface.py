from typing import Protocol, List

from robotix.mind.memory.trace.trace import Trace


class Interface(Protocol):
    """
    
    """
    _traces: List[Trace]
    def _set_traces(self) -> List[Trace]:
        ...
