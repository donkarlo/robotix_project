from mathx.unit.united_scalar_val import UnitedScalar
from robotix.goal.goal import Goal
from robotix.estimation.state import State
from sensorx.state.composite_state import CompositeState


class TimedGoal(Goal):
    def __init__(self, composite_state:CompositeState, time:UnitedScalar):
        self._time = time
        super().__init__(states_list)