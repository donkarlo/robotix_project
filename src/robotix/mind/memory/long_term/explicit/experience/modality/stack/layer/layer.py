from functools import cache
from typing import List, Optional

from robotix.mind.memory.long_term.explicit.episodic.trace.observer.arrival_publisher import ArrivalPublisher as TraceArrivalPublisher
from robotix.mind.memory.long_term.explicit.episodic.trace.observer.arrival_subscriber import ArrivalSubscriber
from robotix.mind.memory.long_term.explicit.episodic.trace.trace import Trace
from utilix.data.storage.decorator.multi_valued.interface import Interface as MultiValuedStorageInterface
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.interface import Interface as DataStorageInterface
from utilix.oop.design_pattern.behavioral.observer.subscriber import Subscriber


class Layer(TraceArrivalPublisher):
    """
    Each current_level is LowerAndHigherAwareLayer should have access to hardware for saving data on it and have ram to keep it in its active memory
    """
    def __init__(self, storage: MultiValuedStorageInterface, next_higher_layer:Optional["Layer"]=None, previous_lower_layer:Optional["Layer"] = None, internal_relator:Optional["Layer"] = None, higher_level_relator: Optional["Layer"] = None, lower_level_relator:Optional["Layer"] = None):
        """
        Every experience has its own storage. a current_level can be formed of multiple experiences. now we just know storages for experiences. That is an experience
        Args:
            storage: Todo: Make storage in utilix composite
            internal_relator: sequence of traces creates what sequence
            higher_level_relator: for example build clusters
            lower_level_relator: for example a decoder that converts a cluster to probable modality_members
        """
        if not storage.isinstance(MultiValued):
            raise TypeError(f"Storage must be an instance of {MultiValued.__name__}")
        self._storage = storage
        self._internal_relator_model = internal_relator
        self._higher_level_relator_model = higher_level_relator
        self._lower_level_relator_model = lower_level_relator

        self._trace_arrival_subscribers: List[Subscriber] = []

        #cache
        self._higher_level_traces:List[Trace] = None

    def add_trace(self, trace: Trace)->None:
        pass

    def attach_trace_arrival_subscriber(self, subscriber: ArrivalSubscriber) -> None:
        self._trace_arrival_subscribers.append(subscriber)

    def detach_trace_arrival_subscriber(self, subscriber: ArrivalSubscriber) -> None:
        self._trace_arrival_subscribers.remove(subscriber)

    def notify_trace_arrival_subscribers(self, trace: Trace) -> None:
        for trace_arrival_subscriber in self._trace_arrival_subscribers:
            trace_arrival_subscriber.do_something_with_new_published_subject(trace)


    def get_storage(self) -> DataStorageInterface:
        return self._storage

    def get_higher_level_relator(self) -> ArrivalSubscriber:
        return self._higher_level_relator_model

    @cache
    def generate_higher_level_traces(self)->List[Trace]:
        self._higher_level_traces = self._higher_level_relator_model.get_entities()
        return self._higher_level_traces