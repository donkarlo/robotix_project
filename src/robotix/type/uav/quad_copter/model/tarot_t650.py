from robotix.plan.mission.mission import Mission
from robotix.type.uav.quad_copter.quad_copter import QuadCopter


class TarotT650(QuadCopter):

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

