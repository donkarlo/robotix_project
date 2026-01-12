from typing import Optional
from robotix.structure.kind.mind.goal.composite.composite import Composite as CompositeGoal
from abc import ABC
from robotix.structure.structure import Structure


class Robot(ABC):
    """
    A robot is a sensor set
    """
    def __init__(self, structure: Structure, name:Optional[str]):
        """

        Args:
            body: includes brain to
            mind: where activity potential fields are converted to meaningful values
            name:
        """
        self._structure = structure
        self.__name = name

    def learn(self)->None:
        pass

    def set_name(self, name:str)->None:
        """
        usualled called ina population of robots
        Args:
            name:

        Returns:

        """
        self.__name = name

    def get_structure(self)->Structure:
        return self._structure

    def get_name(self)->Optional[str]:
        return self.__name

    def get_goal_tree(self)-> CompositeGoal:
        """
        TODO: build it from memory tree
        MUst be taken from memory which is a part of stracture composite
        Returns:
        """
        pass


    def run(self)->None:
        # loading memories
        # if self._mind.get_memory().get
        goal_tree = None
        # TODO: Maybe this should be suprise rate
        # TODO: Goal tree must be build from different locations in memory tree

        goal_tree = self._get_goal_tree()
        #rank according to priorities and mid states
        self._rank_goals()



