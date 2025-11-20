from mathx.linalg.tensor.vector.vector import Vector
from robotix.mind.memory.trace.kind.kind import Kind
from functools import cache

from utilix.data.kind.dic.dic import Dic


class LidarScanRanges(Kind):
    """
    """

    def __init__(self):
        super().__init__("LidarScanRanges")
    @cache
    def get_schema(self) -> Dic:
        trace_kind_schema = \
            {
                "ranges": Vector
            }


