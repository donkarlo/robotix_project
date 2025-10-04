from robotix.spa.plan.mission.mission import Mission


class Spa:
    """
    - Stands for sense-plan-act
    """
    def __init__(self, mission:Mission):
        while True:
            self.sense()
            self.plan()
            self.act()
