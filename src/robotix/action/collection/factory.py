import copy

from robotix.action.action import Action
from typing import List
from utilix.data.storage.type.file.file import File
from utilix.os.path import Path

class Factory:

    @staticmethod
    def from_vecs_file_path(sample_action:Action, vecs_file_path:str, vec_sep: str = "\n", component_sep: str = " ")->List[Action]:
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
        #to support position, pose
        vec_lines = vecs_text.split(vec_sep)
        for vec_line in vec_lines:
            vec_line = vec_line.strip()
            # if the vec_line is empty
            if not vec_line:
                continue
            vec_components = []
            for component in vec_line.split(component_sep):
                vec_components.append(float(component))

            new_action = copy.deepcopy(sample_action)
            new_action.get_goal().get_desired_state().get_vector_representation().set_components(vec_components)
            actions.append(new_action)
        return actions



