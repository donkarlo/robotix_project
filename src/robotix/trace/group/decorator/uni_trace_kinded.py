from robotix.trace.group.decorator.decorator import Decorator
from robotix.trace.group.interface import Interface as TraceGroupInterface
from robotix.trace.group.kind.core.kind import Kind as TraceGroupKind


class UniTraceKinded(Decorator):
    def __init__(self, inner: TraceGroupInterface, kind: TraceGroupKind):
        super().__init__(inner)
        self._kind = kind

    def get_kind(self) -> TraceGroupKind:
        return self._kind