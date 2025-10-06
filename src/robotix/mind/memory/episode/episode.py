from abc import abstractmethod


class  Episode:
    """
    Maybe different from Trigger, I should think about it
    - from what an episode must be composed
        − Mission
            - act (with feed back)
                - commands (one time signals to actuator_set)
            - sensors
    """
    def __init__(self):
        pass

    @abstractmethod
    def get_string(self):
        pass
