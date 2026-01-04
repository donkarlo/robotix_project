from typing import Protocol, runtime_checkable, Any, Optional

from robotix.body.nervous.neuron.collection.population_activity_field import PopulationActivityField


@runtime_checkable
class Interface(Protocol):
    _population_activity_field: Optional[PopulationActivityField]
    _formatted_data: Any

    def __init__(self, population_activity_field: PopulationActivityField):
        ...

    def get_population_activity_field(self) -> PopulationActivityField:
        ...

    def convert_formatted_data_to_population_activity_field(self) -> PopulationActivityField:
        ...
