from robotix.plan.mission.mission import Mission
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet
from robotix.type.uav.quad_copter.quad_copter import QuadCopter
from typing import Optional
from robotix.physical.actuator.type.rotor.rotor import Rotor
from sensorx.collection.collection import Collection
from sensorx.type.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from sensorx.type.gps.odom.sensor import Sensor as GpsOdomSensor
from robotix.mental.cognition.mind import Mind
from robotix.mental.cognition.memory.memory import Memory
from robotix.mental.cognition.memory.memorizing import Memorizing
from robotix.mental.cognition.memory.remembering import Remembering
from robotix.mental.cognition.learning.learning import Learning
from robotix.mental.cognition.memory.long_term.explicit.episodic.experience.collection.collection import \
    Collection as ExperienceCollection


class TarotT650Oldest(QuadCopter):

    def __init__(self, experience_collection: ExperienceCollection, name:Optional[str]=None):
        rotor = Rotor()
        rotor_set = RotorSet(rotor)
        sensor_set = Collection([RpA2Lidar(), GpsOdomSensor()])
        memory = Memory(Memorizing(), Remembering(), experience_collection)
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

