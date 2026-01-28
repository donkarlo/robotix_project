from robotix.structure.kind.mind.action.goal.composite.component import Component
from utilix.oop.design_pattern.structural.composite.composite import Composite as BaseComposite


class Composite(Component ,BaseComposite):
    """
    - As long as a child goal is running, a parent is also considered to be running
    """
    pass