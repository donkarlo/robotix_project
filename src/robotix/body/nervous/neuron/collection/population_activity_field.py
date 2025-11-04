from robotix.body.nervous.neuron.spike.spike import Spike


class PopulationActivityField:
    def __init__(self, spikes:list[Spike]):
        self._spikes = spikes

    def get_aproximate_envoked_time(self):
        pass
    def get_approximate_somatotopic_locations(self):
        pass