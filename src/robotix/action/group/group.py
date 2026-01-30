from typing import List

from robotix.action.composite.component import Component
from utilix.data.kind.group.group import Group as BaseGroup


class Group(BaseGroup):
    def __init__(self, members:List[Component]):
        BaseGroup.__init__(self, members)