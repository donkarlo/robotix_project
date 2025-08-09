from typing import Tuple, List
from sensorx.state.state import State

from robotix.goal.robot_goal import RobotGoal


class Goal:
    '''
    it is formed of several states for example for a quad it can be 3d position, pitch, yaw role
    This is a single action
    '''
    def __init__(self, composit_state:CompositState,parent_goal:Goal=None):
        '''
        Args:
            states_list (list[State]): is the state_list at one time step
        '''
        self._states_list = states_list

        #action history to achive the action
        self._action_history:List = None


