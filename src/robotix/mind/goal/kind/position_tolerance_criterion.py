import math
from robotix.mind.goal.acceptance.criterion import AcceptanceCriterion
from physix.quantity.kind.kinematic.pose.position.position import Position


class PositionToleranceCriterion(AcceptanceCriterion):
    """
    Goal is satisfied if the Euclidean distance between
    current and desired positions is below a threshold.
    """

    def __init__(self, tolerance: float):
        self._tolerance = tolerance

    def is_satisfied(self, current_position: Position, desired_position: Position) -> bool:
        dx = current_position.x - desired_position.x
        dy = current_position.y - desired_position.y
        dz = current_position.z - desired_position.z
        distance = math.sqrt(dx * dx + dy * dy + dz * dz)
        return distance <= self._tolerance
