from typing import Any, Type


class Field:
    def __init__(self, name:str, value:Any, type:Type):
        """

        Args:
            name:
            value:
            type:
        """
        self._name = name
        self._value = value
        self._type = type

    def get_value(self)->Any:
        return self._value

    def get_type(self)->str:
        return self._type

    def get_name(self)->str:
        return self._name