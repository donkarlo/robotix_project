from robotix.spa.plan.mission.mission import Mission


class Spa:
    """
    - Stands for sense-pre_plan-role
    - implements perception(sense), reasoning(pre_plan), control(role)
    """
    def __init__(self, mission:Mission):
        while True:
            self.sense()
            self.plan()
            self.act()
