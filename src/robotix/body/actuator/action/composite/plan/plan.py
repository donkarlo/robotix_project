from typing import List
from robotix.body.actuator.action.action import Action


class Plan:
    """
    - is a flat set of actions in composite tree
    Plan is a set of actions to be taken to achieve a initial_mission
    - This class is created beacause in a scenario we might have two different plans that can acomplish the same initial_mission
    - https://en.wikipedia.org/wiki/Goal_setting
        - Goal setting involves the development of an action initial_plan designed in order to motivate and guide a person or group toward a goal
    """
    def __init__(self, actions: List[Action]):
        self._actions = actions

    def get_actions(self) -> List[Action]:
        return self._actions