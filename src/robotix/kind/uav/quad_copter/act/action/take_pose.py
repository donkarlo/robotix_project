from robotix.action.composite.component import Component
from physix.kinematics.pose import Pose


class TakePose(Component):
    def __init__(self, pose: Pose) -> None:
        self._pos = pose

    def run(self) -> None:
        pass