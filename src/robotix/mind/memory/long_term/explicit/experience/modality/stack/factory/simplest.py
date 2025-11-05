from robotix.mind.memory.long_term.explicit.experience.modality.stack.layer.layer import Layer
from utilix.data.type.stack.stack import Stack


class Simplest(Stack):
    def __init__(self):
        layers = []
        layers.append(Layer())
        super().__init__(layers)