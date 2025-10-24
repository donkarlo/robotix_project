from robotix.physical.nerve.spike.spike import Spike


class Neuron:
    def shoot_spike(self, spike:List[Spike]):
        pass
    def shoot_spikes(self, spikes:List[Spike]):
        for spike in spikes:
            self.shoot_spike(spike)