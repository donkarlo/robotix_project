from typing import List

from robotix.mind.memory.trace.observer.arrival_publisher import ArrivalPublisher as TraceArrivalPublisher
from robotix.mind.memory.trace.observer.creation_subscriber import CreationSubscriber
from robotix.mind.memory.trace.trace import Trace
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedStorageInterface
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.interface import Interface as DataStorageInterface
from utilix.oop.design_pattern.behavioral.observer.subscriber import Subscriber


class Layer(TraceArrivalPublisher):
    """
    Each current_level is LowerAndHigherAwareLayer should have access to hardware for saving data on it and have ram to keep it in its active memory
    """
    def __init__(self, storage: MultiValuedStorageInterface):
        """
        Every experience has its own trace_storage. a current_level can be formed of multiple experiences. now we just know storages for experiences. That is an experience
        Args:
            storage:
        """
        if not storage.isinstance(MultiValued):
            raise TypeError(f"Storage must be an instance of {MultiValued.__name__}")
        self._storage = storage

        self._trace_arrival_subscribers: List[Subscriber] = []


    def add_trace(self, trace: Trace)->None:
        pass

    def attach_trace_arrival_subscriber(self, subscriber: CreationSubscriber) -> None:
        self._trace_arrival_subscribers.append(subscriber)

    def detach_trace_arrival_subscriber(self, subscriber: CreationSubscriber) -> None:
        self._trace_arrival_subscribers.remove(subscriber)

    def notify_trace_arrival_subscribers(self, trace: Trace) -> None:
        for trace_arrival_subscriber in self._trace_arrival_subscribers:
            trace_arrival_subscriber.do_something_with_new_published_subject(trace)


    def get_storage(self) -> DataStorageInterface:
        return self._storage
