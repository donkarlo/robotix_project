from enum import Enum, auto


class Kinds(Enum):
    EXPERIENCE = auto()
    MODALITY = auto()
    #partitioned
    CLASSIFIED = auto()
    SEMANTIC = auto()
    # formed of episodes that answer the question
    EPISODIC = auto()

