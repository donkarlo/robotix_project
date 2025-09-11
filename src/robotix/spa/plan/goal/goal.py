from typing import List
from sensorx.state.state import State


class Goal:
    '''
    it is formed of a state for example for a quad it can be 3d position, pitch, yaw role
    This is a single action
    '''
    def __init__(self, state:State):
        self._state = state


