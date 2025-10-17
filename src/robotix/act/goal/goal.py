from mathx.linalg.vec.vec import Vec
from robotix.act.goal.acceptance_criterion import AcceptanceCriterion
from typing import TypeVar, Generic, Optional

# to cover either state or vectors such as position
VecType=TypeVar('VecType', bound=Vec)

class Goal(Generic[VecType]):
    """
    Represents a target state and its acceptance criterion.
    """

    def __init__(self, desired_state: VecType, acceptance: AcceptanceCriterion):
        self._desired_state = desired_state
        self._acceptance = acceptance

    def is_achieved(self, current_state: VecType) -> bool:
        return self._acceptance.is_satisfied(current_state, self._desired_state)

    def get_desired_state(self) -> VecType:
        return self._desired_state

    def get_acceptance(self) -> AcceptanceCriterion:
        return self._acceptance