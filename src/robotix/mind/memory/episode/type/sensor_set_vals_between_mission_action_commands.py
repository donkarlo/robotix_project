from robotix.mind.memory.episode.episode import Episode
from robotix.spa.action.action import Action
from robotix.spa.action.actuator.command.command import Command
from robotix.spa.plan.mission.mission import Mission
from sensorx.obs.sensor_set_obs_vals import SensorSetObsVals
from mathx.linalg.vec.vec import Vec


class SensorsetValsBetweenMissionActionCommands(Episode):
    """
    multiple sensor data between two consequent commands
    """
    def __init__(self, mission: Mission, action: Action, command: Command):
        self._mission = mission
        self._action = action
        self._command = command

        #init
        self._sensor_set_obs_vals = SensorSetObsVals()

    def add_sensor_set_val(self, val:Vec)->None:
        self._sensor_set_obs_vals.add_sensor_set_val(val)