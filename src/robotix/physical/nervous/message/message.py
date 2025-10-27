from physix.dimension.unit.unit import Unit
from robotix.physical.nerve.neuron import Neuron
from robotix.physical.nerve.spike.spike import Spike


class Message:
    """
    commands, actions, plans, missionssensor obss should be all translatable to episodic\
    - the most comlicated msg is nested key values
    - episodic is episodic only if structurally similllar messages have been seen in the brain of the system
    """
    def __init__(self, nueurons_spikes_times:List[Tuple[Neuron,Spike,float]], time_unit:Unit):
        self._time_unit = time_unit
        self._nueurons_spikes_times = nueurons_spikes_times

    def get_rate(self, unit:Unit)->float:
        """calculate base on frequency of nueurons_spikes_times"""
        pass

    def get_existing_label_or_create_new_label(self)->Morephem:
        pass