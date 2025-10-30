from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from robotix.act.goal.acceptance_criterion import AcceptanceCriterion
from typing import  Optional

class Goal(VectorRepresentable):
    """
    Represents a target state and its acceptance criterion.
    """

    def __init__(self, desired_state: VectorRepresentable, acceptance: AcceptanceCriterion):
        self._desired_state = desired_state
        self._acceptance = acceptance

    def is_achieved(self, current_state: VectorRepresentable) -> bool:
        return self._acceptance.is_satisfied(current_state, self._desired_state)

    def get_desired_state(self) -> VectorRepresentable:
        return self._desired_state

    def get_acceptance(self) -> AcceptanceCriterion:
        return self._acceptance