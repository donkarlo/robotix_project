from robotix.physical.actuator.actuator import Actuator
from typing import Tuple
from typing import Optional


class Collection:
    def __init__(self, actuators:Tuple[Actuator], parent_name:Optional[str]=None, name:Optional[str] = None):
        self.__name = name
        self._parent_id = parent_name
        self._actuators = actuators