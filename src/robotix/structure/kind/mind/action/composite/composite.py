from robotix.structure.kind.mind.action.composite.component import Component
from utilix.oop.design_pattern.structural.composite.composite import Composite as BaseComposite


class Composite(Component, BaseComposite):
    """
    - is a flat set of actions in composite tree
    Composite is a set of actions to be taken to achieve a initial_mission
    - This class is created beacause in a scenario we might have two different plans that can acomplish the same initial_mission
    - https://en.wikipedia.org/wiki/Goal_setting
        - Goal setting involves the development of an action initial_plan designed in order to motivate and guide a person or group toward a goal
    """
    pass