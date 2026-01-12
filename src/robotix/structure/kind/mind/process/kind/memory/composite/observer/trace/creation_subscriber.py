from typing import Protocol, runtime_checkable

from robotix.structure.kind.mind.process.kind.memory.composite.trace.trace import Trace

@runtime_checkable
class TraceCreationSubscriber(Protocol):
    def do_with_created_trace(self, trace: Trace)->None: ...