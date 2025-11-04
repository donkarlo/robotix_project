from robotix.mind.action.action import Action
from physix.quantity.type.kinematic.pose.position.position import Position
from robotix.mind.goal.goal import Goal


class GoTo(Action):
    def __init__(self, position_goal:Goal) -> None:
        if not isinstance(position_goal.get_desired_state(), Position):
            raise TypeError('GoTo: Goal.get_desired_state() must be of describer Position')
        super().__init__(position_goal)

    def run(self) -> None:
        pass