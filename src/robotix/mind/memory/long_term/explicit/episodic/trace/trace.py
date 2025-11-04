from robotix.body.nervous.neuron.collection.population_activity_field import PopulationActivityField as NervousSpikeActivityField
from abc import ABC, abstractmethod
from typing import Optional, Any


class Trace(ABC):
    """
    An role or a sensor read happens
    - this is the boundry between body brain and mind mind
    - spikes can not be decorated or be composite or decorated
    - trace covers from spike activit field to structed data
    - this is the leaf of composite pattern
    """
    def __init__(self, nervous_population_spike_activity_field: NervousSpikeActivityField):
        self._nervous_population_activity_field = nervous_population_spike_activity_field

        # the following data can be approximated when trace is in a population bigger than first current_level episode
        # it is just a point, a data point, without a population it has no meaning
        self._formatted_data:Any = None
        self._time = None
        # is it a command? a lidar sensor? a initial_mission?
        self._type = None

    @abstractmethod
    def set_formatted_data(self, formatted_data:Any)->None:
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

    def get_nervous_population_activity_field(self) -> Optional[NervousSpikeActivityField]:
        return self._nervous_population_activity_field

