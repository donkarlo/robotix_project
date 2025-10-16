import copy

from robotix.act.action import Action
from typing import Generic, TypeVar, Type, List
from utilix.data.storage.type.file.file import File
from mathx.linalg.vec.vec import Vec
from robotix.act.goal.goal import Goal
from utilix.os.path import Path


ActionType = TypeVar("ActionType", bound=Action)
VecType = TypeVar("VecType", bound=Vec)


class CollectionGenerator(Generic[ActionType]):

    @staticmethod
    def get_homos_from_file_path(action_class: Type[ActionType], vec_class:Type[VecType], file_path: str, vec_sep: str = "\n", component_sep: str = " ") -> List[ActionType]:
        """

        Args:
            action_class:
            vec_class: it can be Position or Pose ....
            file_path:
            vec_sep:
            component_sep:

        Returns:

        """
        path = Path(file_path)
        vecs_text = File(path).get_ram().strip()

        actions: List[ActionType] = []
        # optional hook, for example pose is formed of position and quaternion in constructor, so it shoul have this classmethod to build directly from a list of 7 members
        vec_factory = getattr(vec_class, "init_from_components", None)
        vec_lines = vecs_text.split(vec_sep)
        for vec_line in vec_lines:
            vec_line = vec_line.strip()
            #if the vec_line is empty
            if not vec_line:
                continue
            for component in vec_line.split(component_sep):
                vec_components.append(float(component))
            vec:Vec = vec_factory(comps) if callable(vec_factory) else vec_class(comps)
            goal = Goal(vec)
            action = vec_class(comps)
            actions.append(action)
        return actions

    @staticmethod
    def clone_from_vecs_file_path(sample_action:Action, vecs_file_path:str, vec_sep: str = "\n", component_sep: str = " ")->List[Action]:
        """
        Clone multiple Action instances from a file that contains lines of vector components.

        Each line corresponds to one vector. For example:
            -15 15 5
            -14.5 15 5
            -14 15 5

        Parameters:
            sample_action: An example Action object (used to infer Action and Vec types)
            vecs_file_path: Path to the file containing vector data
            vec_sep: Separator between vectors (default newline)
            component_sep: Separator between components of each vector (default space)

        Returns:
            List of cloned Action objects.
        """
        path = Path(vecs_file_path)
        vecs_text = File(path).get_ram().strip()
        actions: List[Action] = []

        vec_class = sample_action.get_goal().get_desired_state().__class__
        #to support position
        vec_factory = getattr(vec_class, "init_from_components", None)
        vec_lines = vecs_text.split(vec_sep)
        for vec_line in vec_lines:
            vec_line = vec_line.strip()
            # if the vec_line is empty
            if not vec_line:
                continue
            vec_components = []
            for component in vec_line.split(component_sep):
                vec_components.append(float(component))
            vec:Vec = vec_factory(vec_components) if callable(vec_factory) else vec_class(vec_components)
            goal_acceptance = copy.deepcopy(sample_action.get_goal().get_acceptance())
            goal = Goal(vec, goal_acceptance)
            action = sample_action.__class__(goal)
            actions.append(action)
        return actions



