
from robotix.structure.kind.mind.world import World
from robotix.spa.plan.mission.interface import Interface as MissionInterface
from robotix.action.composite.composite import Composite
from abc import ABC, abstractmethod


class Planner(ABC):
    def __init__(self, mission:MissionInterface, world:World):
        self._mission = mission
        self._world = world

        # to lazy load a pre_plan
        self._plan:Composite = None

    @abstractmethod
    def get_plan(self)->Composite:
        """
        To return a pre_plan of Actions
        Returns:

        """
        pass