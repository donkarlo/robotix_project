from typing import Protocol, runtime_checkable

from sensorx.collection.collection import Collection as SensorCollection
from sensorx.observation.collection.collection import Collection as ObservationCollection


@runtime_checkable
class StateChangeObserver(Protocol):
    _sensor_collection: SensorCollection
    def get_observations(self, sensor_collection: SensorCollection)-> ObservationCollection:
        """

        Args:
            sensor_collection: all members must be of deocrator Sensored(Observation) so that we know to what sensor it belongs

        Returns:

        """
        ...