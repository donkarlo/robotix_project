from robotix.mind.learn.learn import Learn
from robotix.mind.memory.memory import Memory


class Mind:
    def __init__(self, memory:Memory, learn:Learn):
        self._memory = memory
        self._learn = learn


    def get_learn(self)->Learn:
        return self._learn

    def get_memory(self)->Memory:
        return self._memory
