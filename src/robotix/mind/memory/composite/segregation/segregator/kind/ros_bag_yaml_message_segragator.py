from robotix.mind.memory.composite.composite import Composite as MemoryComposite
from robotix.mind.memory.trace.group.decorator.storaged import Storaged
from robotix.mind.memory.composite.segregation.segregator.segregator import Segregator
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.platform.ros.message.kind.sensor.nav.odometry import Odometry as RosOdometryMessage
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import \
    AddToRamValuesSubscriber as TraceAddValueSubscriber
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_subscriber import \
    GroupRamValuesAdditionFinishedSubscriber
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.type.dic.dic import Dic
from typing import Any
from robotix.platform.ros.message.kind.sensor.lidar.scan.scan import Scan as RosScanMessage
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator
from utilix.oop.inheritance.overriding.override_from import override_from
from robotix.mind.memory.composite.component import Component as MemoryComponent


class RosBagYamlMessageSegragator(Segregator, TraceAddValueSubscriber, GroupRamValuesAdditionFinishedSubscriber):
    """
    Represents the modality group for one experience
    """

    def __init__(self, current_memory_component:MemoryComponent, slc:slice):
        self._loading_slice = slice
        self._current_memory_component = current_memory_component

        if not BaseDecorator.has_decorator(self._current_memory_component.get_trace_group(),
                                           Storaged):
            raise TypeError("Memory component's trace group must be decorated with Storaged")
            if not isinstance(self._current_memory_component.get_trace_group().get_storage(),
                              UniformatedMultiValuedYamlFile):
                raise TypeError("Memory component's trace group storage must be a UniformatedMultiValuedYamlFile")

        # umvyf stand for UniformatedMultiValuedYamlFile
        self._current_umvyf_storage:UniformatedMultiValuedYamlFile = self._current_memory_component.get_trace_group().get_storage()

        #observer subscriptions
        self._current_umvyf_storage.attach_add_to_ram_values_subscriber(self)
        self._current_umvyf_storage.attach_group_ram_values_finished_subscriber(self)

        self._segregated_components:List[MemoryComponent] = []

        # helpers
        self._trace_groups_dic = Dic({})

    @override_from(GroupRamValuesAdditionFinishedSubscriber)
    def do_when_group_ram_values_addition_is_finished(self) ->None:
        for trace_kind, trace_group in self._trace_groups_dic:
            trace_group_storage = UniFormated(MultiValued(File(Path(self._current_umvyf_storage+ self._current_memory_component.get_os_joined_path()))))
            storaged_traced_group = Storaged(trace_group, trace_group_storage)
            self._segregated_components.append(MemoryComposite(storaged_traced_group, trace_kind))



    @override_from(Segregator)
    def segregate(self)->None:
        self._current_umvyf_storage.load_slice(self._loading_slice)

    @override_from(TraceAddValueSubscriber)
    def do_when_a_new_value_is_added_to_ram(self, trace: Any) -> None:
        """Is called from MultiValued storage decorator"""
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

            if trace.get_kind() not in self._trace_groups_dic.get_raw_dict().keys():
                trace_group = TraceGroup(None, trace.get_kind())
                self._trace_groups_dic.add_key_value(trace.get_kind(), trace_group)

            for trace_kind, trace_group in self._trace_groups_dic.get_raw_dict().items():
                if trace_kind == trace.get_kind():
                    trace_group.add_member(trace)


