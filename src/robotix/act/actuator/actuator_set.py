import uuid

from robotix.act.actuator.actuator import Actuator
from typing import Tuple
from typing import Optional


class ActuatorSet:
    def __init__(self, actuators:Tuple[Actuator], parent_id:Optional[str]=None, id:Optional[str] = None):
        self.__id = id
        self._parent_id = parent_id
        self._actuators = actuators