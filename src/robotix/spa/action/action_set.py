from typing import Set

from robotix.spa.action.action import Action


class ActionSet:
    def __init__(self, members:Set[Action]):
        self._members = members