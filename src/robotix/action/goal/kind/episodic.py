"""
Such as scenarios normal, next to, follow etc. So it is goals for when wehere (from Google AI)
"""
from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from robotix.action.goal.acceptance.criterion import AcceptanceCriterion
from robotix.action.goal.goal import Goal


class Episodic(Goal):
    def __init__(self, desired_state: VectorRepresentable, acceptance: AcceptanceCriterion):
        Goal.__init__(self, acceptance)
        self._desired_state = desired_state

    def get_desired_state(self)->VectorRepresentable:
        pass
