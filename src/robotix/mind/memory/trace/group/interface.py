from typing import Protocol, List, runtime_checkable

from robotix.mind.memory.trace.trace import Trace

@runtime_checkable
class Interface(Protocol):
    """
    
    """
    _traces: List[Trace]
    def get_traces(self, traces:List[Trace]) -> List[Trace]:
        ...
