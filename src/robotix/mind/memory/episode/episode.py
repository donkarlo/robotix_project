from abc import abstractmethod
from sensorx.obs.sensor_set_obs.sensor_set_obs_vals import SensorSetObsVals


class  Episode:
    """
    Maybe different from Trigger, I should think about it
    - from what an episode must be composed
        − Mission
        − plan
        - mental world is formed by experoceptive
    """
    def __init__(self, command, sensor_set_vals:SensorSetObsVals):
        pass

    @abstractmethod
    def get_string(self):
        pass
