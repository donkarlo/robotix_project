from typing import Any, List

from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.composite.composite import Composite as MemoryComposite
from robotix.mind.memory.composite.segregation.segregator.segregator import Segregator
from robotix.mind.memory.trace.group.decorator.storaged import Storaged
from robotix.mind.memory.trace.group.decorator.uni_trace_kinded import UniTraceKinded
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from robotix.mind.memory.trace.group.kind.kind import Kind as TraceGroupKind
from robotix.mind.memory.trace.group.kind.kinds import Kinds as TraceGroupKinds
from robotix.platform.ros.message.kind.sensor.lidar.scan.scan import Scan as RosScanMessage
from robotix.platform.ros.message.kind.sensor.nav.odometry import Odometry as RosOdometryMessage
from utilix.data.kind.dic.dic import Dic
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued
from utilix.data.storage.decorator.multi_valued.sliced import Sliced
from utilix.data.storage.decorator.multi_valued.observer.add_to_ram_values_subscriber import \
    AddToRamValuesSubscriber as TraceAddValueSubscriber
from utilix.data.storage.decorator.multi_valued.observer.group_ram_values_addition_finished_subscriber import \
    GroupRamValuesAdditionFinishedSubscriber
from utilix.data.storage.decorator.multi_valued.uni_kinded import UniKinded
from utilix.data.storage.factory.uniformated_multi_valued_yaml_file import UniformatedMultiValuedYamlFile
from utilix.data.storage.kind.file.pkl.pkl import Pkl as PklDataStorage
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator
from utilix.oop.inheritance.overriding.override_from import override_from
from utilix.os.file_system.file.file import File as OsFile
from utilix.os.file_system.path.file import File as FilePath
from utilix.os.file_system.path.directory import Directory as DirPath
from utilix.os.file_system.path.path import Path


class RosBagYamlMessageSegragator(Segregator, TraceAddValueSubscriber, GroupRamValuesAdditionFinishedSubscriber):
    """
    Represents the modality group for one experience
    """

    def __init__(self, current_memory_component: MemoryComponent):
        self._storage_type = "pkl"
        self._current_memory_component = current_memory_component

        if not BaseDecorator.has_decorator(self._current_memory_component.get_trace_group(), Storaged):
            raise TypeError("Working component's trace group must be decorated with Storaged")
        if not isinstance(self._current_memory_component.get_trace_group().get_storage(),
                          UniformatedMultiValuedYamlFile):
            raise TypeError("Working component's trace group storage must be a UniformatedMultiValuedYamlFile")

        # umvyf stand for UniformatedMultiValuedYamlFile
        self._current_uni_formted_multi_value_storage:UniformatedMultiValuedYamlFile = self._current_memory_component.get_trace_group().get_storage()

        # observer subscriptions
        self._current_uni_formted_multi_value_storage.attach_add_to_ram_values_subscriber(self)
        self._current_uni_formted_multi_value_storage.attach_group_ram_values_addition_finished_subscriber(self)

        self._segregated_components: Optional[List[MemoryComponent]] = None

        # helpers, this will be filled when self.do_when_a_new_value_is_added_to_ram is called from uniformated_multi_valued_yaml_file.add_value
        self._trace_groups_dic = Dic({})

    @override_from(GroupRamValuesAdditionFinishedSubscriber)
    def do_when_group_ram_values_addition_is_finished(self) -> None:
        os_sep = Path.get_os_path_separator()

        for trace_kind_name, trace_group in self._trace_groups_dic.get_keys_and_values():
            # Buiding the path for ne File storages
            current_umvyf_storage_str_path = self._current_uni_formted_multi_value_storage.get_native_absolute_string_path()

            current_uni_format_yaml_file_parent_storage_str_path = Path(current_umvyf_storage_str_path).get_parent_directory_string_path()

            segregated_storage_dir_path = DirPath(current_uni_format_yaml_file_parent_storage_str_path + os_sep + trace_group.get_name() + os_sep + trace_group.get_name())

            segregated_storage_file_name = trace_group.get_name() + "." + self._storage_type
            segregated_storage_file_path = FilePath(segregated_storage_dir_path.get_native_os_string_path_with_trailing_slash() + segregated_storage_file_name)

            os_file = OsFile(segregated_storage_file_path, None, None)
            #TODO here multi valued must be replaced with Sliced
            trace_group_storage = UniKinded(MultiValued(PklDataStorage(os_file, create_directory_structure=True), None), trace_kind_name, False)

            storaged_traced_group = Storaged(trace_group, trace_group_storage)
            storaged_traced_group.save()

            segregated_component = MemoryComposite(storaged_traced_group, trace_kind_name)

            self._segregated_components.append(segregated_component)

    @override_from(Segregator)
    def segregate(self) -> None:
        # this envokes TraceAddValueSubscriber.do_when_a_new_value_is_added_to_ram
        self._current_uni_formted_multi_value_storage.load()
        # when finished GroupRamValuesAdditionFinishedSubscriber.do_when_group_ram_values_addition_is_finished

    @override_from(TraceAddValueSubscriber)
    def do_when_a_new_value_is_added_to_ram(self, value: Any) -> None:
        """
        Is called from SlicedValues storage decorator
        """
        if isinstance(value, Dic):
            # if it is a ros message
            if value.has_nested_keys(["header", "frame_id"]):
                # if it is a ROS odom message
                if value.has_nested_keys(["pose"]):
                    # then its is a ROS odometry trace
                    new_trace = RosOdometryMessage.init_from_dic(value).get_distributed_kinematic_trace()


                elif value.has_nested_keys(["ranges"]):
                    # then it is a ROS scan trace
                    new_trace = RosScanMessage.init_from_dic(value).get_scan_ranges_trace()

            # note that trace kind name is the same as trace group kind name in this case
            if new_trace.get_kind().get_name() not in self._trace_groups_dic.get_keys():
                new_trace_group_kind:TraceGroupKind = None
                for available_trace_group_kind in TraceGroupKinds().get_kind_list():
                    if available_trace_group_kind.get_name() == new_trace.get_kind().get_name():
                        new_trace_group_kind = available_trace_group_kind

                new_trace_group = TraceGroup.init_from_traces_and_kind_and_name(None, new_trace_group_kind, new_trace_group_kind.get_name())
                self._trace_groups_dic.add_key_value(new_trace_group.get_name(), new_trace_group, True)

            for trace_group_kind_name, new_trace_group in self._trace_groups_dic.get_keys_values():
                if trace_group_kind_name == new_trace.get_kind().get_name():
                    new_trace_group.add_member(new_trace)
