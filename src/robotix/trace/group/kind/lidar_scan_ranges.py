from robotix.trace.group.kind.core.kind import Kind as GroupTraceKind
from functools import cache
from robotix.trace.kind.lidar_scan_ranges.lidar_scan_ranges import LidarScanRanges as LidarScanRangesTraceKind

from utilix.data.kind.dic.dic import Dic


class LidarScanRanges(GroupTraceKind):
    """
    """

    def __init__(self):
        self._trace_kind: TraceKind = LidarScanRangesTraceKind()
        super().__init__(self._trace_kind.get_name())
    @cache
    def get_schema(self) -> Dic:
        return self._trace_kind.get_schema()


