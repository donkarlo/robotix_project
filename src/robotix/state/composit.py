from typing import Tuple
from mathx.physics.state.state import State


class Composit:
    """For a state formed of other states for examzple [x,y,z] and [raw,pitch,roll]"""
    def __init__(self, states: Tuple[State,...]):
        self._states = states

    def  add_state(self, state:State):
        self._states.append(state)

    def get_concated_state(self):
        #@TODO: Complete later
        pass


