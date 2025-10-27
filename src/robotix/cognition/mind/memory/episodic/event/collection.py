from mathx.numbers.complex.quaternion.quaternion import Quaternion
from mathx.probability.covariance_matrix import CovarianceMatrix
from physix.quantity.type.position import Position
from physix.quantity.type.quaternion_pose import QuaternionPose
from robotix.platform.ros.message.type.header.time_stamp import TimeStamp
from utilix.data.storage.decorator.multi_valued.add_value_observer_protocol import AddValueObserverProtocol
from utilix.data.type.dic.dic import Dic
from typing import Type, Any, List, Dict
from physix.uncertainty.gaussian.timed_pose_distribution import TimedPoseDistribution
from sensorx.type.lidar.rp_a2.obs import Obs as LidarObs


class Collection(AddValueObserverProtocol):

    def __init__(self, classes: List[Type]):
        self._time_unit:Unit = None
        self._events: List[Event] = []
        self._cat_by_type:Dict = {}

    def update(self, event:Any):
        if isinstance(event, Dic):
            # if it is a ROS odom message
            if event.has_nested_keys(["pose", "pose", "position"]):
                pose_dict = event["pose", "pose", "position"]
                position = Position(event["pose", "pose", "position"])
                quaternion = Quaternion()
                qpose = QuaternionPose(position, quaternion)
                cov_mtx = CovarianceMatrix(event[])
                time = TimeStamp.get_time_by_dic(event)
                event = Event(Gaussian(Pose, cov_mtx))
            if event.has_nested_keys(["ranges"]):
                return LidarObs

            self._events.append(event)
