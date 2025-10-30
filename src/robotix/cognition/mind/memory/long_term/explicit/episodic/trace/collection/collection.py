from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.population_filled_trace import PopulationFilledTrace
from robotix.platform.ros.message.type.sensor.nav.odometry import Odometry as RosOdometryMessage
from utilix.data.storage.decorator.multi_valued.add_value_observer_protocol import AddValueObserverProtocol
from utilix.data.type.dic.dic import Dic
from typing import Type, Any, List, Dict, override
from robotix.platform.ros.message.type.sensor.lidar.scan.scan import Scan as RosScanMessage


class Collection(AddValueObserverProtocol):

    def __init__(self, classes: List[Type]):
        self._time_unit:Unit = None
        self._traces: List[Trace] = []
        self._cat_by_trace_type:Dict = {}

    @override
    def add_value_update(self, trace:Any):
        if isinstance(trace, Dic):
            # if it is a ros message
            if trace.has_nested_keys(["header","frame_id"]):
                # if it is a ROS odom message
                if trace.has_nested_keys(["pose"]):
                    #then its is a ROS odometry trace
                    trace = RosOdometryMessage.init_from_dic(trace).get_distributed_kinematic_population_filled_trace()

                if trace.has_nested_keys(["ranges"]):
                    #then it is a ROS scan trace
                    trace = RosScanMessage.init_from_dic(trace).get_scan_ranges_population_filled_trace()

            self._traces.append(trace)
