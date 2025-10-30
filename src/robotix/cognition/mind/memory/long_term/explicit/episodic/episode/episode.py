from abc import abstractmethod
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.trace import Trace
from sensorx.obs.sensor_set_obs.sensor_set_obs_vals import SensorSetObsVals


class  Episode:
    """
    Maybe different from Trigger, I should think about it
    - from what an episodic must be composed
        − Mission
        − plan
        - mental world is formed by experoceptive
    """
    def __init__(self, traces:list[Trace]):
        self._trace = traces

    def get_traces(self):
        return self._trace
