from robotix.experiment.scenario import Scenario


class Experiment:
    """
    We know in a robotic experiment a robot tries to achieve a goal
    """
    def __init__(self, learning_scenarios:tuple[Scenario,...], test_scenarios: tuple[Scenario,...]):
        self._testing_scenarios = test_scenarios
        self._learning_scenarios = learning_scenarios

    def run(self)->None:
        for learning_scenario in self._learning_scenarios:
            learning_scenario.learn()

        for testing_scenario in self._testing_scenarios:
            testing_scenario.test()

