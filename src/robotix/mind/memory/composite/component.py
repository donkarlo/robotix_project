from abc import abstractmethod
from typing import List

from robotix.mind.memory.trace.trace import Trace
from utilix.data.storage.storage import Storage
from utilix.oop.design_pattern.structural.composite.component import Component as BaseComponent


class Component(BaseComponent):
    def __init__(self, trace_storage:Storage):
        self._trace_storage = trace_storage

    def get_storage(self)->Storage:
        return self._trace_storage

    @abstractmethod
    def get_traces(self)->List[Trace]:
        pass