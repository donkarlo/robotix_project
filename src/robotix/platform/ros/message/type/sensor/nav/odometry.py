from functools import cache

from mathx.probability.covariance_matrix import CovarianceMatrix
from physix.quantity.type.kinematic.kinematic import Kinematic
from physix.quantity.decorator.distributed.gaussianed import Gaussianed
from physix.quantity.type.pose.position import Position
from physix.quantity.type.pose.quaternion import Quaternion
from physix.quantity.type.twist.angular import Angular
from physix.quantity.type.twist.linear import Linear
from physix.quantity.type.twist.twist import Twist
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.population_filled_trace import \
    PopulationFilledTrace
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.kind.types import Types
from robotix.platform.ros.message.field.field import Field
from robotix.platform.ros.message.message import Message
from robotix.platform.ros.message.type.header.time_stamp import TimeStamp
from utilix.data.type.dic.dic import Dic
from robotix.platform.ros.message.type.header.header import Header


class Odometry(Message):

    def __init__(self, fields:List):
        super().__init__(fields)
        self._time = self.get_field_value_by_name("time")

    @classmethod
    def init_from_dic(cls, dic: Dic) -> "Odometry":
        # fields
        fields:List[Field] = []

        # time
        time = TimeStamp.get_time_by_dic(dic)
        field = Field("time", time, float)
        fields.append(field)

        # pose
        ## position
        field = Field("position", Dic(dic["pose"]["pose"]["position"]), Dic)
        fields.append(field)

        ## orientation
        field = Field("orientation", Dic(dic["pose"]["pose"]["orientation"]), Dic)
        fields.append(field)

        ## orientation
        field = Field("pose_covarience", Dic(dic["pose"]["covariance"]), Dic)
        fields.append(field)

        # twist
        ## linear
        field = Field("linear_twist", Dic(dic["twist"]["twist"]["linear"]), Dic)
        fields.append(field)

        ## angular
        field = Field("angular_twist", Dic(dic["twist"]["twist"]["angular"]), Dic)
        fields.append(field)

        ## orientation
        field = Field("twist_covarience", Dic(dic["twist"]["covariance"]), Dic)
        fields.append(field)

        return cls(dic)

    @cache
    def get_distributed_kinematic_population_filled_trace(self)-> PopulationFilledTrace:

        #pose
        position_field = self.get_field_value_by_name("position")
        position = Position(position_field["x"], position_field["y"], position_field["z"])

        orientation_field = self.get_field_value_by_name("orientation")
        orientation = Quaternion(orientation_field["x"], orientation_field["y"], orientation_field["z"],
                                 orientation_field["w"])
        pose_cov_field = self.get_field_value_by_name("pose_covarience")
        cov_pose = CovarianceMatrix(pose_cov_field.reshape(6, 6))

        distributed_pose = Gaussianed(Pose(position, orientation), cov_pose)

        #twist
        linear_twist_field = self.get_field_value_by_name("linear_twist")
        linear_twist = Linear(linear_twist_field["x"], linear_twist_field["y"], linear_twist_field["z"])

        angular_twist_field = self.get_field_value_by_name("angular_twist")
        angular_twist = Angular(angular_twist_field["x"], angular_twist_field["y"], angular_twist_field["z"])

        pose_cov_field = self.get_field_value_by_name("twist_covarience")
        cov_twist = CovarianceMatrix(pose_cov_field.reshape(6, 6))

        distributed_pose = Gaussianed(Twist(linear_twist, angular_twist), cov_twist)

        # kinematic
        trace = PopulationFilledTrace(Kinematic(distributed_pose, distributed_twist), self._time , Types.ditributed_kinematic)

        return trace


