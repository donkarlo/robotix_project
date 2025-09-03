from abc import abstractmethod, ABC
from typing import Tuple

from robotix.environment.environment import Environment
from robotix.goal.basic import Basic
from robotix.robot import Robot
class Scenario(ABC):
    """
    Scenario is more than a robot and its goals
    For ecxample it might include the environment state such as walls
    """
    def __init__(self, robot:Robot, goals:Tuple[Basic,...], environment:Environment):
        self._robot = robot
        self._goals = goals
        self._environment = environment

    @abstractmethod
    def run(self) -> None:
        """
        - For example find the leader Robot in an MRS and run it
        - Or run the first goal and then nexts sequentially
        - equally you can run
        Returns:
        """
        pass

    @abstractmethod
    def learn(self):
        pass