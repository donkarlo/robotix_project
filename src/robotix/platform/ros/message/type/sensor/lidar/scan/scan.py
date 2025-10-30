from functools import cache

from mathx.probability.covariance_matrix import CovarianceMatrix
from physix.quantity.decorator.distributed.gaussianed import Gaussianed
from physix.quantity.type.pose.position import Position
from physix.quantity.type.pose.quaternion import Quaternion
from physix.quantity.type.twist.angular import Angular
from physix.quantity.type.twist.linear import Linear
from physix.quantity.type.twist.twist import Twist
from robotix.platform.ros.message.field.field import Field
from robotix.platform.ros.message.message import Message
from robotix.platform.ros.message.type.header.time_stamp import TimeStamp
from sensorx.obs.decorator.timed import Timed
from utilix.data.type.dic.dic import Dic
from robotix.platform.ros.message.type.header.header import Header
from sensorx.type.lidar.obs.obs import Obs as LidarObs
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.kind.types import Types


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
        value = dic["angle_incremenet"]
        field = Field("angle_incremenet", value, "array")
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
        value = dic["intencities"]
        field = Field("intencities", value, "array")
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
        return PopulationFilledTrace(LidarObs(self._fields[ranges]), self._time,
                                     Types.lidar_scan_ranges)
