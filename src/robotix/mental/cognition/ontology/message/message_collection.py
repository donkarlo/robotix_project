from robotix.action.action import Action
from robotix.physical.actuator.command.command import Command
from utilix.data.storage.decorator.multi_valued.add_value_observer_protocol import AddValueObserverProtocol
from utilix.data.type.dic.dic import Dic
from typing import Type
from physix.uncertainty.gaussian.timed_pose_distribution import TimedPoseDistribution
from sensorx.type.lidar.rp_a2.obs import Obs as LidarObs


class MessageCollection(AddValueObserverProtocol):
    message_classes = [Action, PoseDistribution, LidarObs, Command, Plan, Mission]

    def __init__(self, classes:List[Type]):
        self._messages = []
        self._cat_by_type = {}


    def update(self, message:Union[Dic]):
        pass

    def get_message_class(self, message:Dic)->Type:
        if message.has_nested_keys(["pose","pose","position"]):
            return TimedPoseDistribution
        if message.has_nested_keys(["ranges"]):
            return LidarObs