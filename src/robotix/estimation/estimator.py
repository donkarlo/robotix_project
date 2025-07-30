from sensorx.obs.sensor_set_obss import SensorSetObss
from sensorx.state.estimation.estimator import Estimator as SensorEstimator

from robotix.action.action import Action


class Estimator(SensorEstimator):
    '''
    State estimator based on Cmd
    '''
    def __init__(self, sensor_set_obss:SensorSetObss, cmds:list[Action]):
        pass