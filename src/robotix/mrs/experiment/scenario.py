from typing import List
from robotix.spa.plan.mission.robot_mission import RobotMission
from robotix.spa.sense.sensor.robot_sensor import RobotSensor
from robotix.experiment.scenario import Scenario


class Scenario(SingleRobotScenario):
    def __init__(self, robots_missions:Optional[List[RobotMission]]=None, world:Optional[World]=None):
        self.__robots_missions = robots_missions

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
        for robot_mission in self.__robots_missions:
            robot = robot_mission.get_robot()
            mission = robot_mission.get_mission()
            robot.achieve_mission(mission)
        return True


    def load_from(self):
        pass