from functools import cache
from robotix.mind.memory.trace.kind.gaussianed_quaternion_kinematic import GaussianedQuaternionKinematic as GaussianedQuaternionKinematicTraceKind
from robotix.mind.memory.trace.group.kind.core.kind import Kind as GroupTraceKind
from robotix.mind.memory.trace.trace import Trace
from utilix.data.kind.dic.dic import Dic
from typing import List
import numpy as np


class GaussianedQuaternionKinematic(GroupTraceKind):
    """
    """
    def __init__(self):
        self._trace_kind = GaussianedQuaternionKinematicTraceKind()
        super().__init__(self._trace_kind.get_name())

    @cache
    def get_schema(self) -> Dic:
        return self._trace_kind.get_schema()

    def get_time_pose_list(self, records:List[Trace])->np.ndarray:
        for record in records:
            pass

