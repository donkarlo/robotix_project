from functools import cache

from robotix.structure.kind.mind.process.kind.memory.composite.trace.group.kind.lidar_scan_ranges.lidar_scan_ranges import LidarScanRangesTraceKind
from robotix.structure.kind.mind.process.kind.memory.composite.trace.group.kind.gaussianed_quaternion_kinematic.gaussianed_quaternion_kinematic import GaussianedQuaternionKinematic
from robotix.structure.kind.mind.process.kind.memory.composite.trace.group.kind.ros_multi_modal_yaml_messages import RosMultiModalYamlMessages


class Kinds:
    @cache
    def get_kind_list(self):
        kind_list = []
        # add the Finite kinds
        kind_list.append(LidarScanRangesTraceKind())
        kind_list.append(GaussianedQuaternionKinematic())
        kind_list.append(RosMultiModalYamlMessages())

        return kind_list