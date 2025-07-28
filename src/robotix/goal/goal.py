from robotix.state_est.state import State


class Goal:
    '''
    A goal is formed of several states for example for a quad it can be 3d position, pitch, yaw role
    This is a single goal
    '''
    def __init__(self, states_list:tuple[State,...]):
        '''
        Args:
            states_list (list[State]): is the state_list at one time step
        '''
        self._states_list = states_list