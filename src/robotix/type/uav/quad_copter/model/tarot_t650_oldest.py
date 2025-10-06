from robotix.plan.mission.mission import Mission
from robotix.type.uav.quad_copter.act.actuator.rotor_set import RotorSet
from robotix.type.uav.quad_copter.quad_copter import QuadCopter
from typing import List, Optional
from robotix.act.actuator.type.rotor.rotor import Rotor
from sensorx.sensor_set import SensorSet
from sensorx.type.lidar.rp_a2.sensor import Sensor as RpA2Lidar
from sensorx.type.gps.odom.sensor import Sensor as GpsOdomSensor
from robotix.mind.memory.level.levels import Levels
from robotix.mind.memory.level.level import Level
from utilix.data.storage.storage import Storage
from robotix.mind.mind import Mind
from robotix.mind.memory.memory import Memory
from robotix.mind.memory.memorizing import Memorizing
from robotix.mind.memory.remembering import Remembering
from robotix.mind.learn.learn import Learn


class TarotT650Oldest(QuadCopter):

    def __init__(self, level_0_storage:Storage, id:Optional[str]=None):
        rotor = Rotor()
        rotor_set = RotorSet(rotor)
        sensor_set = SensorSet([RpA2Lidar(), GpsOdomSensor()])
        memory_levels = Levels([Level(level_0_storage)])
        memory = Memory(Memorizing(), Remembering(), memory_levels)
        mind = Mind(memory, Learn())
        super().__init__(rotor_set, sensor_set, mind, id)

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

