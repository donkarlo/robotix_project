from typing import Any

from robotix.structure.kind.mind.goal.action.composite.component import Component


class SendMessage(Component):
    def __init__(self, message:Any):
        self._message = message