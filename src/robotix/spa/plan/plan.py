from robotix.spa.plan.goal.goal_interface import GoalInterface as GoalInterface


class Plan(GoalInterface):
    def __init__(self, goal: GoalInterface):
        self._goal = goal