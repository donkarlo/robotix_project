from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace import Trace
from sensorx.observation.interface import Interface as SensorObsInterface

class Sensor(Trace):
    def __init__(self, sensor_obs: SensorObsInterface):
        self._sensor_obs = sensor_obs