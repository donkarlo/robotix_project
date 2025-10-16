from typing import Optional, List, Tuple
from abc import ABC
from robotix.plan.plan import Plan
from robotix.plan.mission.mission import Mission
from robotix.robot import Robot
from physix.world.world import World


class Scenario(ABC):
    """
    Scenario is more than a robot and its missions
    For ecxample it might include the world mission_state such as walls
    """

    def __init__(self, robots_missions_plans:List[Tuple[Robot,Mission,Plan]], world: World, name: Optional[str] = None):
        """

        Args:
            robots_missions_plans:
            world:
            name:
        """
        self._robots_missions_plans = robots_missions_plans

        self._world = world
        self._name = name

        # run

    def run(self) -> None:
        self._robot.achieve_mission(self._mission)

    def learn(self):
        self._robot.learn()

    def get_world(self) -> World:
        return self._world

    def get_missions(self, robot_name:str) -> Mission:
        for robot, mission, plan in self._robots_missions_plans:
            if robot.get_name() == robot_name:
                return mission

    def get_robots(self) -> List[Robot]:
        robots = []
        for robot, mission, plan in self._robots_missions_plans:
            robots.append(robot)

    def get_plans(self, robot_name: str) -> Robot:
        for robot, mission, plan in self._robots_missions_plans:
            if robot.get_name() == robot_name:
                return plan

    def get_name(self) -> str:
        return self._name