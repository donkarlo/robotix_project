from functools import cache
from robotix.trace.kind.gaussianed_quaternion_kinematic.gaussianed_quaternion_kinematic import GaussianedQuaternionKinematic as GaussianedQuaternionKinematicTraceKind
from robotix.trace.group.kind.core.kind import Kind as GroupTraceKind
from robotix.trace.trace import Trace
from utilix.data.kind.dic.dic import Dic
from typing import List
import numpy as np

from utilix.data.storage.kind.file.pkl.pkl import Pkl
from utilix.os.file_system.file.file import File
from utilix.os.file_system.path.path import Path


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

    def get_position_sequence(self)->np.ndarray:
        # ----- Load LiDAR scans -----
        path = Path(
            "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/uav1/mind/memory/explicit/long_term/episodic/experiences/normal/gaussianed_quaternion_kinematic_sliced_from_1_to_300000/gaussianed_quaternion_kinematic_sliced_from_1_to_300000.pkl"
        )

        os_file = File.init_from_path(path)
        pickle = Pkl(os_file, False)
        scan_sliced_values = pickle.load()
        scan_values = scan_sliced_values.get_values()

        positions_sequence = []
        for scan_value in scan_values:
            positions_sequence.append(
                scan_value
                .get_formatted_data()
                .get_pose()
                .get_position()
                .get_vector_representation()
                .get_components()
            )

        positions_sequence = np.array(positions_sequence, dtype=np.float64)
        return positions_sequence
if __name__ == "__main__":
    o = GaussianedQuaternionKinematic()
    print(o.get_position_sequence())


