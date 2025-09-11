from typing import List

from robotix.mrs.mrs import Mrs
from robotix.robot import Robot


class LeaderFollower(Mrs):
    def __init__(self, leader:Robot, followers:List[Robot]):
        self._leader = leader
        self._followers = followers
