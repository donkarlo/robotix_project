from robotix.type.uav.quad_copter.action.action import Action
from robotix.type.uav.quad_copter.state.full_pose import FullPose


class GoTo(Action):
    def __init__(self, full_pose:FullPose) -> None:
        self._pos = pos