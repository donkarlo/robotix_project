from typing import Any

from robotix.mind.action.action import Action


class SendMessage(Action):
    def __init__(self, message:Any):
        self._message = message