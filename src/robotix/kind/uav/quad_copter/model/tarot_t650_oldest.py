from robotix.structure.kind.mind.action.goal.composite.goal import Goal
from robotix.kind.uav.quad_copter.act.actuator.rotor_set import RotorSet
from robotix.kind.uav.quad_copter.quad_copter import QuadCopter
from typing import Optional
from robotix.structure.kind.body.actuator.kind.rotor.rotor import Rotor
from robotix.structure.kind.body.sensor.kind.group.group import Group
from robotix.structure.kind.body.sensor.kind.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from robotix.structure.kind.body.sensor.kind.gps.odom.sensor import Sensor as GpsOdomSensor
from robotix.structure.kind.mind.mind import Mind
from robotix.mind.cognition.process.kind.memory.kind.working.working import Working
from robotix.mind.cognition.process.kind.memory.memorizing.memorizing import Memorizing
from robotix.mind.cognition.process.kind.memory.remembering.remembering import Remembering
from robotix.structure.kind.mind.learning.learning import Learning
from robotix.mind.cognition.process.kind.memory.kind.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup


class TarotT650Oldest(QuadCopter):

    def __init__(self, experience_group:ExperienceGroup, name:Optional[str]=None):
        rotor = Rotor()
        rotor_set = RotorSet(rotor)
        sensor_set = Group([RpA2Lidar(), GpsOdomSensor()])
        memory = Working(Memorizing(), Remembering(), experience_group)
        mind = Mind(memory, Learning())
        super().__init__(rotor_set, sensor_set, mind, name)

    def build_from_urdf(self, urdf: str) -> None:
        super().build_from_urdf(urdf)

    def achieve_mission(self, mission: Goal) -> bool:
        return True

    def on_sensor_obs(self):
        pass

    def on_mission_change(self):
        pass

    def learn(self):
        pass

