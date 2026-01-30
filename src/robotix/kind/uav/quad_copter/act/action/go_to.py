from robotix.action.composite.component import Component
from physix.quantity.kind.dynamic.kinematic.pose.position.position import Position
from robotix.action.goal.goal import Goal


class GoTo(Component):
    def __init__(self, position_goal:Goal) -> None:
        if not isinstance(position_goal.get_desired_state(), Position):
            raise TypeError('GoTo: Goal.get_desired_state() must be of describer TimePosition')
        super().__init__(position_goal)

    def run(self) -> None:
        pass