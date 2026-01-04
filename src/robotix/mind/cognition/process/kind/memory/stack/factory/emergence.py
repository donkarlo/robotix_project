from typing import List

from robotix.mind.cognition.process.kind.memory.stack.layer.layer import Layer
from utilix.data.storage.storage import Storage
from utilix.data.kind.stack.stack import Stack


class Emergence(Stack):
    def __init__(self, storages:List[Storage]):
        layers = []
        layers.append(Layer())
        super().__init__(layers)