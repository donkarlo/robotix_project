from robotix.robot import Robot


class Follower(Robot):
    '''
    Each follower knows its leader as a child-parent relationship
    '''
    def __init__(self, leader:Robot):
        self._leader = leader