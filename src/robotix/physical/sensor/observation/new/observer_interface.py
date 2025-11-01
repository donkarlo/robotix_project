from typing import Protocol

from sensorx.observation.observation import Observation


class Observer(Protocol):
    def new_observation_arrival_update(self, observation:Observation)->None: ...