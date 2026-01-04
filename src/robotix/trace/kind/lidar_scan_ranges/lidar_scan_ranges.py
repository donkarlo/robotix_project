from mathx.linalg.tensor.vector.vector import Vector
from robotix.trace.kind.core.kind import Kind
from functools import cache

from utilix.data.kind.dic.dic import Dic


class LidarScanRanges(Kind):
    """
    """

    def __init__(self):
        super().__init__("lidar_scan_ranges")
    @cache
    def get_schema(self) -> Dic:
        trace_kind_schema = \
            {
                "ranges": Vector
            }


