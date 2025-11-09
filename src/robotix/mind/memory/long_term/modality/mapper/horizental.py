from typing import List

from robotix.mind.memory.long_term.modality.modality import Modality
from robotix.mind.memory.stack.layer.layer import Layer


class Horizental:
    """
    maps one layer (mostly of the same depth) of one modality to another
        - for example maps lidar data to gps
    """
    def __init__(self, mapper, input_modality_layer:List[Modality, Layer], output_modality_layer:List[Modality, Layer]):
        self._mapper = mapper
        self._input_modality_layer = input_modality_layer
        self._output_modality_layer = output_modality_layer