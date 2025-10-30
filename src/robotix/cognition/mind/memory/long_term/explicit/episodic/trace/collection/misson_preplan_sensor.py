from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.collection.collection import Collection
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.population_filled_trace import \
    PopulationFilledTrace
from robotix.cognition.mind.memory.long_term.explicit.episodic.trace.trace import Trace
from robotix.platform.ros.message.type.sensor.nav.odometry import Odometry as RosOdometryMessage
from utilix.data.storage.decorator.multi_valued.add_value_observer_interface import AddValueObserverInterface
from utilix.data.type.dic.dic import Dic
from typing import Type, Any, List, Dict, override
from robotix.platform.ros.message.type.sensor.lidar.scan.scan import Scan as RosScanMessage
from robotix.plan.mission.mission import Mission
from robotix.plan.plan import Plan


class MissionPrePlanSensor(Collection, AddValueObserverInterface):

    def __init__(self, mission:Mission, plan:Plan):
        self._time_unit: Unit = None
        self._distance_unit = None
        self._velocity_unit = None

        self._traces: List[Trace] = []
        self._cat_by_trace_type: Dic = Dic({})

    @override
    def add_value_update(self, trace: Any):
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
    def get_traces(self)->List[Trace]:
        return self._traces