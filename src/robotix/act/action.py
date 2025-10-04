from abc import ABC, abstractmethod
from robotix.act.goal.goal import Goal

class Action(ABC):
    """
    Acording to ROS2: Actions are one of the communication types in ROS 2 and are
    intended for long running missions. They consist of three parts: a act, feedback, and a result.
    - Action is assessable
    - It is also an abstraction. what we call a verb in NLP
    - MAVLINK defines actions
    - if an act is breakable to smaller actions then it is actually a Mission
    - History will be kept in episodes
    """
    def __init__(self, goal:Goal):
        self._goal = goal

    @abstractmethod
    def run(self):
        pass