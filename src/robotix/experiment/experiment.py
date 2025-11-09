from robotix.experiment.scenario import Scenario
from typing import List

from robotix.robot import Robot


class Experiment:
    """
    We know in a robotic experiment a robot tries to achieve a initial_mission
    """

    def __init__(self, robot:Robot, learning_scenarios: List[Scenario], testing_scenarios: List[Scenario]):
        self._robot = robot
        self._testing_scenarios = testing_scenarios
        self._learning_scenarios = learning_scenarios

        # do the experiment
        self.learn()
        self.test()


    def learn(self) -> None:
        for scenario in self._learning_scenarios:
            scenario.learn()

    def test(self) -> None:
        for scenario in self._testing_scenarios:
            scenario.test()

