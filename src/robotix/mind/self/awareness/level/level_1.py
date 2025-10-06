from robotix.mind.self.awareness.level.level import Level
from typing import Annotated, List, override

UnitInterval = Annotated[float, "0.0 ≤ x ≤ 1.0"]


# -------------------------
# Level 1 – Perceptual self-recognition / agency via contingencies
# -------------------------
class Level1(Level):
    """
    Detects correlations between self-generated actions and sensory consequences.
    """

    def test_sensorimotor_contingency(self) -> UnitInterval:
        """
        Measures how well the agent detects that its actions reliably cause
        specific proprioceptive/exteroceptive changes (closed-loop predictability).
        """
        return 0.0

    def test_body_schema_adaptation(self) -> UnitInterval:
        """
        Assesses on-the-fly adaptation of a body schema (e.g., tool use, payload change),
        measured by prediction error reduction after a perturbation.
        """
        return 0.0

    def test_agency_detection(self) -> UnitInterval:
        """
        Quantifies 'sense of agency' (e.g., intentional binding / reduced delay estimates)
        by comparing owned vs. externally injected actuation patterns.
        """
        return 0.0

    @override
    def run_tests(self) -> List[float]:
        v1 = self.test_sensorimotor_contingency()
        v2 = self.test_body_schema_adaptation()
        v3 = self.test_agency_detection()
        return [v1, v2, v3]