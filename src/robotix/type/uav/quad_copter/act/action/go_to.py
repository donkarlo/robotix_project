from robotix.act.action import Action
from physix.kinematics.position import Position
from robotix.act.goal.goal import Goal


class GoTo(Action):
    def __init__(self, position_goal:Goal) -> None:
        if not isinstance(position_goal.get_desired_state(), Position):
            raise TypeError('GoTo: Goal.get_desired_state() must be of type Position')
        super().__init__(position_goal)

    def run(self) -> None:
        pass