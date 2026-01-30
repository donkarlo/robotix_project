from robotix.action.goal.goal import Goal


class Homeostasis(Goal):
    def __init__(self):
        self._rate = 100
    def get_rate(self)->float:
        return self._rate