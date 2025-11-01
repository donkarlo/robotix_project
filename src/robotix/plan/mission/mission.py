from typing import List, Optional
from robotix.sense.state.state import State
from robotix.action.goal.goal import Goal

class Mission:
    '''
    it is formed of a state for example for a quad it can be 3d position, pitch, yaw role
    This is a single role
    - Mission is not a tangibeable concept. Action is tangeable. DeliverMission or CorridorInspectionMission. But Action needs tangeable points and in the world such as GoTo point.
    - if an role is breakable to smaller actions then it is actually a mission
    '''
    def __init__(self, goals:List[Goal], id:Optional[str]=None):
        self._goals = goals