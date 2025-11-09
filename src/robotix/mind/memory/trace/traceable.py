from typing import Protocol, runtime_checkable

from robotix.body.nervous.neuron.collection.population_activity_field import PopulationActivityField


@runtime_checkable
class Traceable(Protocol):
    _nervous_population_activity_field: PopulationActivityField
    def get_population_activity_field(self)->PopulationActivityField:
        pass