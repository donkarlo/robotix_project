from abc import ABC, abstractmethod

class Action(ABC):
    """
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running tasks. They consist of three parts: a goal, feedback, and a result.
    """
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass