from robotix.body.nervous.neuron.collection.population_activity_field import PopulationActivityField
from typing import Any

from robotix.mind.memory.long_term.explicit.episodic.trace.trace import Trace


class PopulationFilledTrace(Trace):
    def __init__(self, formatted_data:Any, time:float, type:int):
        """
        time and role are already determined by a population of activity field from example by ROS
        Args:
            formatted_data: 
            time: 
            type: 
        """
        self._formatted_data = formatted_data
        self._time = time
        self._type = type

    def get_formatted_data(self) -> Any:
        return self._formatted_data

    def get_time(self) -> float:
        return self._time

    def get_type(self) -> int:
        return self._type

    def convert_to_population_acrtivity_field(self, decoder)->PopulationActivityField:
        pass

    def set_time(self, time:float) -> None:
        self._time = time

    def set_type(self, type:int) -> None:
        self._type = type

    def set_formatted_data(self, formatted_data:Any) -> None:
        self._formatted_data = formatted_data