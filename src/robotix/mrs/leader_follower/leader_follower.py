from robotix.mrs.leader_follower.follower import Follower
from robotix.robot import Robot


class LeaderFollower:
    def __init__(self, leader:Robot, followers:list[Follower,...]):
        self._leader = leader
        self._followers = followers
