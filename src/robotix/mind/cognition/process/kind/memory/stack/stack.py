from robotix.mind.cognition.process.kind.memory.stack.layer.layer import Layer
from typing import List, Optional

from robotix.mind.cognition.process.kind.memory.stack.layer.kind.shared_lowest_level import SharedLowestLevel

class Stack:
    #the layer to include all traces without any classification for all the experiences
    shared_lowest_level: SharedLowestLevel
    def __init__(self, layers: Optional[List[Layer]]):
        """
        sorted from bottom or most basic to to most detailed with more clusters and causality relations

        current layering strategy for each modality. from loawest to highest
            - shared between a modality group: lowest layer: neural potential activity fields
            - shared between a modality group: next layer: un categorized traces. here we jave data such as Dic with labeled fields
            - modality specifif layer: next
            - current_level[0] is for raw data such as those for ros messages in topic file, it usually includes _traces without attributing them to any episodes
            - current_level[1] memory>episodic>episodic>group based: changing representation of data and storing it


        Args:
            layers:
        """
        self._layers = layers if layers is not None else []

    def add_layer(self, layer:Layer)->None:
        self._layers.append(layer)

    def get_layers(self) -> List[Layer]:
        return self._layers

    def get_lowest_layer(self) -> Layer:
        lowest_layer = self._layers[0]
        return lowest_layer

    def get_highest_layer(self) -> Layer:
        highest_layer = self._layers[-1]
        return highest_layer

    def __getitem__(self, index:int)->Layer:
        return self._layers[index]