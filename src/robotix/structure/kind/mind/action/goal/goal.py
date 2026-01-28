from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from robotix.structure.kind.mind.action.goal.acceptance.criterion import AcceptanceCriterion
from robotix.structure.kind.mind.action.goal.composite.component import Component


class Goal(Component, VectorRepresentable):
    """
    - Each mental process has a goal. the most important goal at the top of the goal tree in composite pattern is to continousely reduce free energy to keep homeostatus to continue to survive. this is true from cells to human and must be true in robots too
    Represents a bottom state and its acceptance criterion.
    - https://en.wikipedia.org/wiki/Goal
        - A goal or objective is an idea of the future or desired result that a person or a group of people envision, initial_plan, and commit to achieve.
    for goal setting (Composite)
    - Goal setting involves the development of an action initial_plan designed in order to motivate and guide a person or group toward a goal
    """

    def __init__(self,  acceptance: AcceptanceCriterion):
        self._acceptance = acceptance
        self._achievement_rate = 0

    def is_achieved(self, current_state: VectorRepresentable) -> bool:
        return self._acceptance.is_satisfied(current_state, self._desired_state)

    def get_desired_state(self) -> VectorRepresentable:
        return self._desired_state

    def get_acceptance(self) -> AcceptanceCriterion:
        return self._acceptance

    def get_achievemnent_rate(self)->float:
        return self._achievement_rate