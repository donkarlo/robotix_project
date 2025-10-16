from typing import List

from robotix.act.action import Action


class ActionCollection:
    def __init__(self, members:List[Action]):
        self._members = members