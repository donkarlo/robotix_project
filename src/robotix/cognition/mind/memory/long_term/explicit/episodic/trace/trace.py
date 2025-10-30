from robotix.physical.nervous.neuron.collection.population_activity_field import PopulationActivityField as NervousSpikeActivityField
from abc import ABC, abstractmethod
from typing import Any, Optional


class Trace(ABC):
    """
    An action or a sensor read happens
    - this is the boundry between physical brain and mental mind
    - spikes can not be decorated or be composite or decorated
    - trace covers from spike activit field to structed data
    """
    def __init__(self, nervous_spike_activity_field: NervousSpikeActivityField):
        self._nervous_spike_activity_field = nervous_spike_activity_field

        # the following data can be approximated when trace is in a population bigger than first level episode
        self._formatted_data = None
        self._time = None
        # is it a command? a lidar sensor? a mission?
        self._type = None

    @abstractmethod
    def set_formatted_data(self)->None:
        """will comes from higher levels such as clusters or experiences etc"""
        pass

    @abstractmethod
    def set_type(self) -> None:
        """will comes from higher levels such as clusters or experiences etc"""
        pass

    @abstractmethod
    def set_time(self) -> None:
        """will comes from higher levels such as clusters or experiences etc"""
        pass

    def get_nervous_spike_activity_field(self) -> Optional[NervousSpikeActivityField]:
        return self._nervous_spike_activity_field