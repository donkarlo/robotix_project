from typing import List, Protocol, runtime_checkable

from robotix.mind.memory.long_term.explicit.episodic.trace.observer.arrival_subscriber import ArrivalSubscriber
from robotix.mind.memory.long_term.explicit.episodic.trace.trace import Trace

@runtime_checkable
class ArrivalPublisher(Protocol):
    _trace_arrival_subscribers: List[ArrivalSubscriber]

    def attach_trace_arrival_subscriber(self, subscriber: ArrivalSubscriber) -> None: ...

    def detach_trace_arrival_subscriber(self, subscriber: ArrivalSubscriber) -> None: ...

    def notify_trace_arrival_subscribers(self, trace: Trace) -> None: ...