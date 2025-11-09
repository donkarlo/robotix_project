from typing import List

from robotix.mind.memory.stack.layer.layer import Layer
from utilix.data.storage.storage import Storage
from utilix.data.type.stack.stack import Stack


class Emergence(Stack):
    def __init__(self, storages:List[Storage]):
        layers = []
        layers.append(Layer())
        super().__init__(layers)