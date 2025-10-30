from functools import cache

from mathx.probability.covariance_matrix import CovarianceMatrix
from physix.quantity.decorator.distributed.gaussianed import Gaussianed
from robotix.platform.ros.message.field.field import Field
from robotix.platform.ros.message.message import Message
from robotix.platform.ros.message.type.header.time_stamp import TimeStamp
from utilix.data.type.dic.dic import Dic
from robotix.platform.ros.message.type.header.header import Header
from sensorx.type.lidar.observation.observation import Observation as LidarObservation
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.type.types import Types
from typing import List
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.population_filled_trace import \
    PopulationFilledTrace


class Scan(Message):
    def __init__(self, fields:List[Field]):
        super().__init__(fields)
        if self.get_field_value_by_name("ranges") is None or self.get_field_value_by_name("time") is None:
            raise ValueError("ranges must be between field._name s")
        self._time = self.get_field_value_by_name("time")

    @classmethod
    def init_from_dic(cls, dic: Dic) -> "Scan":


        fields = []

        #time
        time = TimeStamp.get_time_by_dic(dic)
        field = Field("time", time, float)
        fields.append(field)

        ##
        value = dic["angle_min"]
        field = Field("angle_min", value, "array")
        fields.append(field)

        ##
        value = dic["angle_max"]
        field = Field("angle_max", value, "array")
        fields.append(field)

        ##
        value = dic["angle_increment"]
        field = Field("angle_increment", value, "array")
        fields.append(field)

        ##
        value = dic["range_min"]
        field = Field("range_min", value, "array")
        fields.append(field)

        ##
        value = dic["range_max"]
        field = Field("range_max", value, "array")
        fields.append(field)

        ##
        value = dic["ranges"]
        field = Field("ranges", value, "array")
        fields.append(field)

        ##
        value = dic["intensities"]
        field = Field("intensities", value, "array")
        fields.append(field)

        return cls(fields)

    @cache
    @staticmethod
    def is_this_message_type_from_dic(dic: Dic) -> bool:
        if not dic.has_nested_keys(["ranges"]):
            return False
        return True

    @cache
    def get_scan_ranges_population_filled_trace(self)-> PopulationFilledTrace:
        return PopulationFilledTrace(LidarObservation(self.get_field_value_by_name("ranges")), self._time,
                                     Types.lidar_scan_ranges)
