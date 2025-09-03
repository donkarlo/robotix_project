from typing import Tuple, List
from sensorx.state.state import State

from robotix.goal.robot_goal import RobotGoal


class Basic:
    '''
    it is formed of several states for example for a quad it can be 3d position, pitch, yaw role
    This is a single action
    '''
    def __init__(self, state:State):
        self._state = state

        #action history to achive the action
        self._action_history:List = None


