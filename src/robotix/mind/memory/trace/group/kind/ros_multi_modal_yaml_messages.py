from robotix.mind.memory.trace.group.kind.core.kind import Kind as GroupTraceKind
from utilix.data.kind.dic.dic import Dic
from utilix.oop.inheritance.overriding.override_from import override_from


class RosMultiModalYamlMessages(GroupTraceKind):
    def __init__(self):
        super().__init__("RosMultiModalYamlMessages")

    @override_from(GroupTraceKind)
    def get_schema(self) ->Dic:
        schema = Dic({})
        return schema