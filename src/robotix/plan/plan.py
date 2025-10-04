from typing import List

from robotix.act.action import Action


class Plan:
    """
    Plan is a set of actions to be taken to achieve a mission
    - This class is created beacause in a scenario we might have two different plans that can acomplish the same mission
    """
    def __init__(self, actions: List[Action]):
        self._actions = actions

    def get_actions(self) -> List[Action]:
        return self._actions