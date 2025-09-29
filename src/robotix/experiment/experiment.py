from robotix.experiment.scenario import Scenario
from typing import List


class Experiment:
    """
    We know in a robotic experiment a robot tries to achieve a goal
    """

    def __init__(self, learning_scenarios: List[Scenario], testing_scenarios: List[Scenario]):
        self._testing_scenarios = testing_scenarios
        self._learning_scenarios = learning_scenarios


    def learn(self) -> None:
        for scenario in self._learning_scenarios:
            scenario.learn()

    def test(self) -> None:
        for scenario in self._testing_scenarios:
            scenario.test()

