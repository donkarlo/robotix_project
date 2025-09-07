from typing import List
from sensorx.state.state import State


class Goal:
    '''
    it is formed of several states for example for a quad it can be 3d position, pitch, yaw role
    This is a single action
    - Goal is a final goal_state given to a plan to achieve it
    '''
    def __init__(self, state:State):
        self._state = state

        #action history to achive the action
        self._action_history:List = None


