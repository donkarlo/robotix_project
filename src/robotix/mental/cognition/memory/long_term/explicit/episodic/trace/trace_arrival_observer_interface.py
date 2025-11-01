from typing import Protocol, runtime_checkable

from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace import Trace

@runtime_checkable
class TraceArrivalObserverInterface(Protocol):
    def do_with_arrived_trace(self, trace: Trace)->None: ...