from abc import ABC, abstractmethod

class Action(ABC):
    """
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running tasks. They consist of three parts: a action, feedback, and a result.
    - An action is verb.
    - A goal is an adverb
    - Action is not what is spoken to an actuator
    """
    def __init__(self):
        # th
        self.__command_history = []

    @abstractmethod
    def run(self):
        pass