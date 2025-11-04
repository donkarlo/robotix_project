from robotix.body.brain.theory.bayesian.free_energy.active_inference import ActiveInference
from robotix.body.brain.theory.bayesian.free_energy.preceptual_inference import PreceptualInference


class FreeEnergy:
    """
    https://en.wikipedia.org/wiki/Free_energy_principle
    """
    def __init__(self):
        self._free_energy_value = None

    def try_minimize(self, active_inference:ActiveInference, perceptual_inference: PreceptualInference)->float:
        """
        usein active inference strategy and perceptual inference strategy free energy must be minimized
        Args:
            active_inference:
            perceptual_inference:

        Returns:

        """
        pass

    def get_free_energy_value(self, hiddden_states:State, obss:Obss)->float:
        return self._free_energy_value