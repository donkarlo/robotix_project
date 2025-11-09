from robotix.platform.ros.message.type.sensor.nav.odometry import Odometry as RosOdometryMessage
from utilix.data.storage.decorator.multi_valued.add_to_ram_values_subscriber import AddToRamValuesSubscriber as TraceAddValueSubscriber
from utilix.data.type.dic.dic import Dic
from typing import Any, override
from robotix.platform.ros.message.type.sensor.lidar.scan.scan import Scan as RosScanMessage
from robotix.mind.memory.long_term.modality.group.group import Group as ModalityGroup


class BaseLayerBuilder(ModalityGroup, TraceAddValueSubscriber):
    """
    Represents the modality group for one experience
    """

    def __init__(self):
        pass

    @override(TraceAddValueSubscriber)
    def add_to_ram_values_update(self, trace: Any)->None:
        if isinstance(trace, Dic):
            # if it is a ros message
            if trace.has_nested_keys(["header", "frame_id"]):
                # if it is a ROS odom message
                if trace.has_nested_keys(["pose"]):
                    # then its is a ROS odometry trace
                    trace = RosOdometryMessage.init_from_dic(trace).get_distributed_kinematic_population_filled_trace()


                elif trace.has_nested_keys(["ranges"]):
                    # then it is a ROS scan trace
                    trace = RosScanMessage.init_from_dic(trace).get_scan_ranges_population_filled_trace()

            self._cat_by_trace_type.add_key_value(trace.get_type(), trace, True)
            self._traces.append(trace)


    def get_one_layered_modality_group(self)->Dic:
        return self._cat_by_trace_type