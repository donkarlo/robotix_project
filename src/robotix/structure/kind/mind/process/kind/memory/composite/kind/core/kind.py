from enum import Enum, auto


class Kind(Enum):
    """
    Goal kinds
    """
    SINGLE_SENSOR_SEQUENCE = auto()
    