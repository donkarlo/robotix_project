from robotix.action.action import Action


class ActionSequence:
    def __init__(self, cmd_sq:list[Action,...]):
        self._cmd_sq = cmd_sq


