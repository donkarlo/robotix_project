from typing import List
from robotix.robot import Robot


class LeaderFollower:
    def __init__(self, leader:Robot, followers:List[Robot]):
        self._leader = leader
        self._followers = followers
