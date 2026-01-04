from robotix.mind.cognition.process.kind.memory.stack.layer.layer import Layer


class Intra:
    def __init__(self, lower_layer:Layer, next_higher_layer:Layer):
        self._lower_layer = lower_layer
        self._next_higher_layer = next_higher_layer