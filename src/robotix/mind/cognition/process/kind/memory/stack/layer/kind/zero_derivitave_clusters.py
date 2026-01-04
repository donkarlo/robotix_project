from fontTools.otlLib.optimize.gpos import Cluster

from robotix.mind.cognition.process.kind.memory.stack.layer.layer import Layer
from utilix.data.storage.storage import Storage


class ZeroDerivitaveClusters(Layer):
    def __init__(self, storage:Storage, clusters:list[Cluster]):
        super().__init__(storage)
        self._clusters = clusters

    def get_clusters(self):
        pass