from typing import Any

from robotix.action.composite.component import Component


class SendMessage(Component):
    def __init__(self, message:Any):
        self._message = message