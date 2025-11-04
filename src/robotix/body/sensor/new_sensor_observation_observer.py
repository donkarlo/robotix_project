from typing import Protocol

from sensorx.observation.observation import Observation


class NewSensorObservationObserver(Protocol):
    def attach_new_sensor_observation_observer(self, observation:Observation)->None:
        pass