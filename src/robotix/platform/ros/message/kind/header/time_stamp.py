from functools import cache

from physix.quantity.type.time import Time
from physix.dimension.unit.unit import Unit

from utilix.data.type.dic.dic import Dic
class TimeStamp:
    def __init__(self, seconds:int, nano_seconds:int):
        self._second = seconds
        self._nano_second = nano_seconds
        super().__init__([Field(self._second, int), Field(self._nano_second, int)])
        self._time = Time(self._second + self._nano_second/ 1e9, Unit("s"))

    @classmethod
    def init_from_message_dic(cls, dic: Dic) -> "TimeStamp":
        stamp = message_dic["header"]["stamp"]
        second = stamp["secs"]
        nano_second = stamp["nsecs"]
        return cls(second, nano_second)

    @staticmethod
    @cache
    def get_time_by_dic(dic:Dic)->float:
        stamp = dic["header"]["stamp"]
        time =  stamp["secs"] + stamp["nsecs"] / 1e9, Unit("s")
        return time

    def get_time(self)->Time:
        return self._time
