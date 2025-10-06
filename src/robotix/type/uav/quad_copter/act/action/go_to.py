from robotix.act.action import Action
from physix.kinematics.pose import Pose


class GoTo(Action):
    def __init__(self, pose:Pose) -> None:
        self._pos = pose

    def run(self) -> None:
        pass