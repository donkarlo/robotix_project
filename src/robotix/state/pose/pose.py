from mathx.physics.dimension.state.pose.point import Point
from mathx.physics.dimension.state.pose.quaternion import Quaternion

from robotix.state.state import State


class Pose(State):
    def __init__(self, point:Point, quaternion:Quaternion):
        self._point = point
        self._quaternion = quaternion