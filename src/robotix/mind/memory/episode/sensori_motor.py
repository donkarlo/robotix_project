from typing import Tuple

from mathx.physics.unit.unit import Unit
from sensorx.obs.sensor_set_obss import SensorSetObss

from robotix.spa.action.action import Action
from robotix.spa.action.actuator.command.command import Command
from robotix.spa.plan.goal.goal import Goal


class SensoriMotor(Unit):
    """
    This unit episode says each memory unit is formed of a goal for which multiple actions should be performed so that acc
    - The main probllem here is that we dont know after a set of commands in the meiddle how long should we expecting the forthcomming sensory observations are related. maybe clustering can do this
    """
    def __init__(self, goal:Goal, action:Action, prv_obss:SensorSetObss, commands:Tuple[Command,...], next_obss:SensorSetObss):
        self._goal = goal
        self._action = action
        self._prv_obss = prv_obss
        self._commands = commands
        self._next_obss = next_obss
