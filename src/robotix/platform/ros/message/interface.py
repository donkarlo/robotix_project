from typing import Protocol, List, Any

class Interface(Protocol):
    _fields = List[Any]
    @classmethod
    def init_from_dic(cls, dic: Dic): ...