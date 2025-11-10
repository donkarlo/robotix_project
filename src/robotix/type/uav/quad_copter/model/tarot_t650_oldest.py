from robotix.mind.goal.composite.mission.mission import Mission
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet
from robotix.type.uav.quad_copter.quad_copter import QuadCopter
from typing import Optional
from robotix.body.actuator.type.rotor.rotor import Rotor
from sensorx.collection.collection import Collection
from sensorx.type.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from sensorx.type.gps.odom.sensor import Sensor as GpsOdomSensor
from robotix.mind.mind import Mind
from robotix.mind.memory.memory import Memory
from robotix.mind.memory.memorizing.memorizing import Memorizing
from robotix.mind.memory.remembering.remembering import Remembering
from robotix.mind.learning.learning import Learning
from robotix.mind.memory.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup


class TarotT650Oldest(QuadCopter):

    def __init__(self, experience_group:ExperienceGroup, name:Optional[str]=None):
        rotor = Rotor()
        rotor_set = RotorSet(rotor)
        sensor_set = Collection([RpA2Lidar(), GpsOdomSensor()])
        memory = Memory(Memorizing(), Remembering(), experience_group)
        mind = Mind(memory, Learning())
        super().__init__(rotor_set, sensor_set, mind, name)

    def build_from_urdf(self, urdf: str) -> None:
        super().build_from_urdf(urdf)

    def achieve_mission(self, mission: Mission) -> bool:
        return True

    def on_sensor_obs(self):
        pass

    def on_mission_change(self):
        pass

    def learn(self):
        pass

