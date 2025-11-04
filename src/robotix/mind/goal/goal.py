from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from robotix.mind.goal.acceptance_criterion import AcceptanceCriterion


class Goal(VectorRepresentable):
    """
    Represents a target state and its acceptance criterion.
    - https://en.wikipedia.org/wiki/Goal
        - A goal or objective is an idea of the future or desired result that a person or a group of people envision, initial_plan, and commit to achieve.
    for goal setting (Plan)
    - Goal setting involves the development of an action initial_plan designed in order to motivate and guide a person or group toward a goal
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