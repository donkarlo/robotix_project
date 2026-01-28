from typing import List, Optional
from robotix.structure.kind.mind.action.goal.goal import Goal as BaseGoal

class Goal(BaseGoal):
    '''
    TODO: should be replaced with a higher level goal and
    it is formed of a state for example for a quad it can be 3d position, pitch, yaw role
    This is a single role
    - Goal is not a tangibeable concept. Goal is tangeable. DeliverMission or CorridorInspectionMission. But Goal needs tangeable points and in the world such as GoTo point.
    - if an role is breakable to smaller actions then it is actually a initial_mission
    '''
    def __init__(self, goals:List[BaseGoal], name:Optional[str]=None):
        self._goals = goals
        self._name = name