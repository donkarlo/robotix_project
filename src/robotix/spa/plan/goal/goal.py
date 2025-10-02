from typing import List

from robotix.state.state import State

class Goal:
    '''
    it is formed of a state for example for a quad it can be 3d position, pitch, yaw role
    This is a single action
    - Goal is not a tangibeable concept. Action is tangeable. DeliverGoal or CorridorInspectionGoal. But Action needs tangeable points and in the world such as GoTo point.
    - if an action is breakable to smaller actions then it is actually a goal
    '''
    def __init__(self, states:List[State]):
        self._states = states