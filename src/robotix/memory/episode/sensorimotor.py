from sensorx.obs.sensor_set_obss import SensorSetObss


class SensoriMotor(Unit):
    """
    This unit episode says each memory unit is formed of a goal for which multiple actions should be performed so that acc
    - The main probllem here is that we dont know after a set of commands in the meiddle how long should we expecting the forthcomming sensory observations are related. maybe clustering can do this
    """
    def __init__(self, goal:Goal, action:Action, prv_obss:SensorSetObss, commands:Tuple[Command,...], next_obss:SensorSetObss):
        self._goal = goal
        self._action = action
        self._prv_obss = prv_obss
        self._next_obss = next_obss
