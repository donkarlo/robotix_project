from typing import Tuple

from mathx.physics.unit.unit import Unit
from sensorx.obs.sensor_set_obss import SensorSetObss

from robotix.spa.action.action import Action
from robotix.spa.action.actuator.command.command import Command
from robotix.spa.plan.mission.mission import Mission


class SensoriMotor(Unit):
    """
    This unit episodic says each memory unit is formed of a mission for which multiple actions should be performed so that acc
    - The main probllem here is that we dont know after a set of commands in the meiddle how long should we expecting the forthcomming sensory observations are related. maybe clustering can do this
    """
    def __init__(self, mission:Mission, action:Action, prv_obss:SensorSetObss, commands:Tuple[Command,...], next_obss:SensorSetObss):
        self._mission = mission
        self._action = action
        self._prv_obss = prv_obss
        self._commands = commands
        self._next_obss = next_obss
