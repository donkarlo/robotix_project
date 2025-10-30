from robotix.plan.mission.mission import Mission
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet
from robotix.type.uav.quad_copter.quad_copter import QuadCopter
from typing import Optional
from robotix.act.actuator.type.rotor.rotor import Rotor
from sensorx.sensor_set import SensorSet
from sensorx.type.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from sensorx.type.gps.odom.sensor import Sensor as GpsOdomSensor
from robotix.cognition.mind.mind import Mind
from robotix.cognition.mind.memory.memory import Memory
from robotix.cognition.mind.memory.memorizing import Memorizing
from robotix.cognition.mind.memory.remembering import Remembering
from robotix.cognition.mind.learn.learn import Learn
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.collection.collection import \
    Collection as ExperienceCollection


class TarotT650Oldest(QuadCopter):

    def __init__(self, experience_collection: ExperienceCollection, name:Optional[str]=None):
        rotor = Rotor()
        rotor_set = RotorSet(rotor)
        sensor_set = SensorSet([RpA2Lidar(), GpsOdomSensor()])
        memory = Memory(Memorizing(), Remembering(), experience_collection)
        mind = Mind(memory, Learn())
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

