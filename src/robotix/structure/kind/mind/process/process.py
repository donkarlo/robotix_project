"""
https://en.wikipedia.org/wiki/Category:Mental_processes
"""
from abc import ABC, abstractmethod


class Process(ABC):
    """
    Each mental process has a goal. the most important goal at the top of the goal tree in composite pattern is to continousely reduce free energy to keep homeostatus to continue to survive. this is true from cells to human and must be true in robots too
    """
    pass
    @abstractmethod
    def activate(self):
        pass