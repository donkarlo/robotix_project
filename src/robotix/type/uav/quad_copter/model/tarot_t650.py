from robotix.spa.plan.goal.goal import Goal
from robotix.type.uav.quad_copter.quad_copter import QuadCopter


class TarotT650(QuadCopter):
    def __init__(self):
        pass

    def build_from_urdf(self, urdf: str) -> None:
        super().build_from_urdf(urdf)

    def achieve_goal(self, goal: Goal) -> bool:
        pass

    def on_sensor_obs(self):
        pass

    def on_goal_change(self):
        pass

    def learn(self):
        pass

