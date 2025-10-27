from typing import Any


class Field:
    def __init__(self, name:str, value:Any, type:str):
        self._name = name
        self._value = value
        self._type = type

    def get_value(self)->Any:
        return self._value

    def get_type(self)->str:
        return self._type

    def get_name(self)->str:
        return self._name