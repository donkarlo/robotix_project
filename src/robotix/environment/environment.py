from utilityx.conf.conf import Conf


class Environment:
    """
    Environment is of two types:
    - What it really is for testing from the human pointv of view which in reality it doesnt exist
    - What the robot think of it with algorithms such as SLAM
    """
    def __init__(self):
        self._occupany_grid_map = None

    def build_from_sdf(self, sdf:str):
        """
        Building from Gazebo sdf
        """
        pass