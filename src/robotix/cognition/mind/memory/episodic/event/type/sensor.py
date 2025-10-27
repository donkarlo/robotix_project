from sensorx.obs.interface import Interface as SensorObsInterface

class Sensor(Event):
    def __init__(self, sensor_obs: SensorObsInterface):
        self._sensor_obs = sensor_obs