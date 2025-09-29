from typing import List
from robotix.spa.plan.goal.robot_goal import RobotGoal
from robotix.spa.sense.sensor.robot_sensor import RobotSensor
from robotix.experiment.scenario import Scenario


class Scenario(SingleRobotScenario):
    def __init__(self, robots_goals:Optional[List[RobotGoal]]=None, world:Optional[World]=None):
        self.__robots_goals = robots_goals

    def learn(self)->None:
        pass

    def run(self, robots_sensors_to_save:List[RobotSensor]=None) -> bool:
        """"

        Args:
            robots_sensors_to_save:
        Returns:

        """
        if robots_sensors_to_save!=None:
            # @TODO: the code on ros to save the topics for sensors in robots_sensors_to_save
            # Probably needs to call a bash script here.
            pass
        for robot_goal in self.__robots_goals:
            robot = robot_goal.get_robot()
            goal = robot_goal.get_goal()
            robot.achieve_goal(goal)
        return True


    def load_from(self):
        pass