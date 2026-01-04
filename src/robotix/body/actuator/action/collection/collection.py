from typing import List

from robotix.body.actuator.action.action import Action


class Collection:
    def __init__(self, members:List[Action]):
        self._members = members