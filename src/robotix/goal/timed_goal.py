from mathx.unit.united_scalar_val import UnitedScalar
from robotix.goal.goal import Goal
from robotix.estimation.state import State


class TimedGoal(Goal):
    def __init__(self, states_list:tuple[State,...], time:UnitedScalar):
        self._time = time
        super().__init__(states_list)