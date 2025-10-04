
from robotix.mind.world import World
from robotix.spa.plan.mission.interface import Interface as MissionInterface
from robotix.plan.plan import Plan
from abc import ABC, abstractmethod


class Planner(ABC):
    def __init__(self, mission:MissionInterface, world:World):
        self._mission = mission
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