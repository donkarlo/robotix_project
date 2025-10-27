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
from utilix.data.type.dic.dic import Dic
from robotix.platform.ros.message.type.header.header import Header
from sensorx.type.lidar.obs.value import Value as ScanObsSensorValue


class Scan(Message):
    def __init__(self, fields:List[Field]):
        super().__init__(fields)

    @classmethod
    def init_from_dic(cls, dic: Dic) -> Dic:
        time = TimeStamp.get_time_by_dic()

        # twist
        start_angle = dic["angle_min"]
        end_angle = dic["angle_max"]
        angle_incremenet = dic["angle_increment"]
        range_min = dic["range_min"]
        range_max = dic["range_max"]
        ranges = dic["ranges"]
        intencities = dic["intencities"]
        ranges_field = Field("ranges", "values", "array")
        fields = [ranges_field]
        return fields

    def get_scan_sensor_obs_value(self)-> ScanObsSensorValue:
        pass
