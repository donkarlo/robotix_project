from robotix.platform.ros.message.composite.component import Component
from robotix.platform.ros.message.interface import Interface
from typing import List, Any, Optional
from abc import ABC, abstractmethod
from robotix.platform.ros.message.field.field import Field
from robotix.platform.ros.message.type.header.header import Header
from utilix.data.type.dic.dic import Dic
from functools import cache


class Message(Component, ABC, Interface):
    """
    This is the leaf of the composite.
    - Message in ros can be formed of nested messages.
    """
    def __init__(self, fields:List[Field] = None):
        self._fields = fields


    @abstractmethod
    @classmethod
    def init_from_dic(cls, dic:Dic)->"Message": ...

    def add_field(self, field:Field)->None:
        self._fields.append(field)

    @cache
    def get_field_value_by_name(self, id:str)->Optional[Any]:
        for field in self._fields:
            if field.get_name() == id:
                return field.value






