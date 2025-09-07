from typing import List

from robotix.spa.sense.sensor.sensor import Sensor


class SensorSet:
    '''
    Sensors of the same parent for example member_sensors of a robot
    '''
    def __init__(self, member_sensors: List[Sensor]):
        '''
        For example a GPS and LIDAR in a Robot. But it can be a set of related member_sensors for some reason event in multiple robots
        :param member_sensors:
        '''
        #@todo either it should be a set of sets or set of member_sensors
        # if the member_sensors do not have ids automatically generate unique ids
        self._memeber_sensors = member_sensors

    def __str__(self):
        print ("To print member_sensors")