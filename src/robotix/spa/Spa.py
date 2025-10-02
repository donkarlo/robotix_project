from robotix.spa.plan.goal.goal import Goal


class Spa:
    """
    - Stands for sense-plan-action
    """
    def __init__(self, goal:Goal):
        while True:
            self.sense()
            self.plan()
            self.act()
