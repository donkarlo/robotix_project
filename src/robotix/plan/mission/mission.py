from typing import List

from robotix.sense.state.state import State

class Mission:
    '''
    it is formed of a state for example for a quad it can be 3d position, pitch, yaw role
    This is a single act
    - Mission is not a tangibeable concept. Action is tangeable. DeliverMission or CorridorInspectionMission. But Action needs tangeable points and in the world such as GoTo point.
    - if an act is breakable to smaller actions then it is actually a mission
    '''
    def __init__(self, states:List[State]):
        self._states = states