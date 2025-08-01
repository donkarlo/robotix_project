from robotix.mrs.type.leader_follower.follower import Follower
from robotix.robot import Robot


class LeaderFollowers:
    def __init__(self, leader:Robot, followers:list[Follower,...]):
        self._leader = leader
        self._followers = followers
