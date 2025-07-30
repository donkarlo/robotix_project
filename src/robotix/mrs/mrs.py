from src.robotix.robot import Robot


class Mrs:
    '''A set of robots whose states are inter related through commands'''
    def __init__(self, robot_members:set[Robot]):
        self._robots_members = robot_members

    def add_robot(self, robot:Robot)->None:
        # TODO: check for uniquness
        self._robots_members.append(robot)

    def get_robots_members(self)->list[Robot,...]:
        return self._robots_members