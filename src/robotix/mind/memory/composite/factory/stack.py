from utilix.data.type.stack.stack import Stack
from typing import List
from robotix.mind.memory.composite.composite import Composite as CompositeMemory

class Stack:
    def __init__(self, names:List[str]):
        self._names = names
        comp_mems: List[CompositeMemory] = []
        for comp_counter, name in enumerate(names):
            cur_comp = CompositeMemory(None, name)
            comp_mems.append(cur_comp)
            if comp_counter > 0:
                comp_mems[-2].add_child(cur_comp)

        self._root_composite = comp_mems[0]
        self._deepest_composite = comp_mems[-1]

    def get_root_composite(self) -> CompositeMemory:
        return self._root_composite

    def get_deepest_composite(self) -> CompositeMemory:
        return self._deepest_composite
