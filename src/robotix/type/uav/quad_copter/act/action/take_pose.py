from robotix.action.action import Action
from physix.kinematics.pose import Pose


class TakePose(Action):
    def __init__(self, pose: Pose) -> None:
        self._pos = pose

    def run(self) -> None:
        pass