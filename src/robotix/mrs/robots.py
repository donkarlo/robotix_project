from src.robotix.robot import Robot


class Robots:
    def __init__(self, robots_list:list[Robot,...]):
        self._robots_list = robots_list

    def add_robot(self, robot:Robot)->None:
        self._robots_list.append(robot)

    def get_robots_list(self)->list[Robot,...]:
        return self._robots_list