from robotix.action.action import Action


class ActionSequence:
    def __init__(self, action_sequence:list[Action,...]):
        self._action_sequence = action_sequence


