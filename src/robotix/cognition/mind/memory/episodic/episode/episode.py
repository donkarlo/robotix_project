from abc import abstractmethod
from robotix.cognition.mind.memory.episode.event.event import Event
from sensorx.obs.sensor_set_obs.sensor_set_obs_vals import SensorSetObsVals


class  Episode:
    """
    Maybe different from Trigger, I should think about it
    - from what an episodic must be composed
        − Mission
        − plan
        - mental world is formed by experoceptive
    """
    def __init__(self, event:List[Event]):
        pass

    @abstractmethod
    def get_string(self):
        pass
