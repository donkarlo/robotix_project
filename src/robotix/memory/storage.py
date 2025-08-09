from abc import abstractmethod
from utilityx.data.source import Source

class Storage(Source):
    def __init__(self):
        pass

    @abstractmethod
    def save_by_unit(self):
        pass

    @abstractmethod
    def load(self):
        pass