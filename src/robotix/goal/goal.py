from typing import Tuple, List
from sensorx.state.state import State

from robotix.goal.robot_goal import RobotGoal


class Goal:
    '''
    A goal is formed of several states for example for a quad it can be 3d position, pitch, yaw role
    This is a single goal
    '''
    def __init__(self, states_list:Tuple[State,...]):
        '''
        Args:
            states_list (list[State]): is the state_list at one time step
        '''
        self._states_list = states_list

        #action history to achive the goal
        self._action_history:List = None

    def achieve(self) -> None:
        pass

