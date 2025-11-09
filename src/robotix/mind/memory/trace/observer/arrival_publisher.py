from typing import List, Protocol, runtime_checkable

from robotix.mind.memory.trace.observer.creation_subscriber import CreationSubscriber
from robotix.mind.memory.trace.trace import Trace

@runtime_checkable
class ArrivalPublisher(Protocol):
    _trace_arrival_subscribers: List[CreationSubscriber]

    def attach_trace_arrival_subscriber(self, subscriber: CreationSubscriber) -> None: ...

    def detach_trace_arrival_subscriber(self, subscriber: CreationSubscriber) -> None: ...

    def notify_trace_arrival_subscribers(self, trace: Trace) -> None: ...