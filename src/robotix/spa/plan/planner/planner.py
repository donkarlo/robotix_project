
from robotix.mind.world import World
from robotix.spa.plan.goal.interface import Interface as GoalInterface
from robotix.spa.plan.plan import Plan
from abc import ABC, abstractmethod


class Planner(ABC):
    def __init__(self, goal:GoalInterface, world:World):
        self._goal = goal
        self._world = world

        # to lazy load a plan
        self._plan:Plan = None

    @abstractmethod
    def get_plan(self)->Plan:
        """
        To return a plan of Actions
        Returns:

        """
        pass