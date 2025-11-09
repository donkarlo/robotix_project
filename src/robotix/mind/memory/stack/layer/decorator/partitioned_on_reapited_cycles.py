from typing import List, Optional

from robotix.mind.memory.stack.layer.decorator.decorator import Decorator
from robotix.mind.memory.stack.layer.interface import \
    Interface as LayerInterface
from robotix.mind.memory.trace.trace import Trace


class PartitionedOnReapitedCycles(Decorator):
    """
    Has partitioned one modality of an experience into repeating cycles
    """
    def __init__(self, inner:LayerInterface, cycles:Optional[List]=None):
        super(Decorator, self).__init__(inner)
        self._cycles:List[Trace] = cycles

    def get_cycles(self)-> Optional[List]:
        return self._cycles