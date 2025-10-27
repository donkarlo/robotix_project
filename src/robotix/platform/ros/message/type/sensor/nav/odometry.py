from mathx.probability.covariance_matrix import CovarianceMatrix
from physix.quantity.type.kinematic.kinematic import Kinematic
from physix.quantity.decorator.distributed.gaussianed import Gaussianed
from physix.quantity.type.pose.position import Position
from physix.quantity.type.pose.quaternion import Quaternion
from physix.quantity.type.twist.angular import Angular
from physix.quantity.type.twist.linear import Linear
from physix.quantity.type.twist.twist import Twist
from robotix.platform.ros.message.message import Message
from robotix.platform.ros.message.type.header.time_stamp import TimeStamp
from utilix.data.type.dic.dic import Dic
from robotix.platform.ros.message.type.header.header import Header


class Odometry(Message):

    @classmethod
    def init_from_dic(cls, dic: Dic) -> Dic:
        time = TimeStamp.get_time_by_dic()

        # twist
        linear_twist = Linear(dic["twist", "twist", "linear"])
        angular_twist = Angular(dic["twist", "twist", "angular"])
        cov_twist = CovarianceMatrix(np.ndarray(dic["twist", "covariance"]).reshape(6, 6))
        distributed_twist = Gaussianed(Twist(linear_twist, angular_twist), cov_twist)

        # pose
        position_msg = dic["pose"]["pose"]["position"]
        orientation_msg = dic["pose"]["pose"]["orientation"]
        position = Position(position_msg["x"], position_msg["y"], position_msg["z"])
        orientation = Quaternion(orientation_msg["x"], orientation_msg["y"], orientation_msg["z"], orientation_msg["w"])
        cov_pose = CovarianceMatrix(np.ndarray(Dic["twist", "covariance"]).reshape(6, 6))
        distributed_pose = Gaussianed(Pose(position, orientation), cov_pose)

        #kinematics
        kinematic = Kinematic(distributed_pose, distributed_twist)


        dic = Dic({"time":time,"kinematics": kinematic})

        return dic
