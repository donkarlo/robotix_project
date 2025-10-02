from abc import ABC, abstractmethod

class Action(ABC):
    """
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running tasks. They consist of three parts: a action, feedback, and a result.
    - Action is assessable
    - It is also an abstraction. what we call a verb in NLP
    - MAVLINK defines actions
    - if an action is breakable to smaller actions then it is actually a Goal
    - History will be kept in episodes
    """
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass