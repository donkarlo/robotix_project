from typing import List

from robotix.mrs.group import Group
from robotix.robot import Robot


class LeaderFollower(Group):
    def __init__(self, leader:Robot, followers:List[Robot]):
        self._leader = leader
        self._followers = followers
