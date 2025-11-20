from robotix.mind.memory.stack.stack import Stack as LayerStack


class Modality:
    def __init__(self, stack:LayerStack, name:str):
        """
        For example modelity for only lidar, modality for only gps odom, modality for autoencoded_3d_lidar_and_gps, or extracted features etc of gps such as curvture
        - modelity can be used both by explicit and implicit memory. also, inside explisit memoru, it can join experience to semantic.


        Args:
            stack:
            name:
        """
        self._layer_stack = stack
        self.__name = name
    def get_name(self)->str:
        return self.__name

    def get_stack(self)->LayerStack:
        return self._layer_stack

