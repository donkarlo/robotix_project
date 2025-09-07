from typing import Protocol

from robotix.spa.plan.goal.goal_interface import GoalInterface


class PlanInterface(Protocol):
    goal: GoalInterface