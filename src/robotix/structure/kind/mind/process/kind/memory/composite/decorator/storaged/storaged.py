# from robotix.structure.mind.process.kind.memory.composite.decorator.decorator import Decorator as CompositeMemoryDecorator
# from robotix.structure.mind.process.kind.memory.composite.trace.group.group import Finite as TraceGroup
# from utilix.data_set.storage.decorator.multi_valued.slices_cashed_interface import \
#     Interface as MultiValuedStorageInterface
# from utilix.data_set.storage.interface import Interface as StorageInterface
#
#
# class Storaged(CompositeMemoryDecorator, StorageInterface):
#     """
#     TODO: Must handle bothe the internal_storage in composite from which some trace groups might have derived and also all the trace groups which have internal_storage that they must and I must fix it
#     - We keep this because we will have working mempory that will not have any storage in most cases
#     """
#
#     def __init__(self, inner: CompositeMemoryDecorator, internal_storage:StorageInterface):
#         """
#         The internal_storage in storaged is brain or physical part of the mind
#         """
#         CompositeMemoryDecorator.__init__(self, inner)
#         self._internal_storage = internal_storage
#         # here we connect by reference the ram of internal_storage and the mambers of the trace group
#         self._internal_storage.set_ram(inner.get_members())
#
#     def get_internal_storage(self) -> MultiValuedStorageInterface:
#         return self._internal_storage
#
#     def save(self) -> None:
#
#         self._internal_storage.save()
#
#     def load(self) -> None:
#         self._internal_storage.load()