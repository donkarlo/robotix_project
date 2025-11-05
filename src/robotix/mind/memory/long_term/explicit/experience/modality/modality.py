from robotix.mind.memory.long_term.explicit.experience.modality.stack.stack import Stack as LayerStack


class Modality:
    def __init__(self, stack:LayerStack, name:str):
        """
        For example modelity for only lidar, modality for only gps odom, modality for autoencoded_3d_lidar_and_gps, or extracted features etc of gps such as curvture
        Args:
            stack:
            name:
        """
        self._stack = stack
        self.__name = name
    def get_name(self)->str:
        return self.__name

    def get_stack(self)->LayerStack:
        return self._stack

