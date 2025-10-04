from typing import Set

from robotix.act.action import Action


class ActionSet:
    def __init__(self, members:Set[Action]):
        self._members = members