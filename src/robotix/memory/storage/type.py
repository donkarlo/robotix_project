from abc import ABC


class Type(Enum):
    def __init__(self, id: str):
        self.__id = id
