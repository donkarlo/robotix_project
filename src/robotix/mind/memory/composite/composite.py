from robotix.mind.memory.composite.component import Component as MemoryComponent
from robotix.mind.memory.trace.group.group import Group as TraceGroup
from utilix.oop.design_pattern.structural.composite.composite import Composite as BaseComposite
from utilix.os.file_system.path.path import Path


class Composite(MemoryComponent, BaseComposite):
    def __init__(self, trace_group:TraceGroup, name:str):
        """

        Args:
            trace_group: can be None to only host the link (child) to the next leaf (trace group here) or composite (only link/child or a trace group)
            name:
        """
        MemoryComponent.__init__(self, trace_group, name)
        BaseComposite.__init__(self, name)

    def create_directory_structure(self, root_path:Path, leaf_file_extension: str) -> None:
        """
        For each Composite: create a directory named after the composite under `root_path`.
        For each Leaf: create a file named `leaf.get_name() + leaf_file_extension` inside its parent directory.
        This proceeds recursively for nested composites.
        Existing directories/files are left intact.
        Notes:
            - two equal traces in two different components may have different meanings
        """
        import os

        def create_file(file_path: Path) -> None:
            if not file_path.file_exists():
                # Guarantee parent directories exist (defensive)
                parent = os.path.dirname(file_path.get_native_absolute_path())
                if parent and not os.path.isdir(parent):
                    os.makedirs(parent, exist_ok=True)
                with open(file_path.get_native_absolute_path(), "w", encoding="utf-8"):
                    pass

        # Directory for this composite under root_path
        dir_name = self.get_name()
        dir_abs = os.path.join(root_path.get_native_absolute_path(), dir_name)
        dir_path = Path(dir_abs)
        if not dir_path.directory_exists():
            dir_path.create_missing_directories()

        # Create files for direct leaves and recurse into composite children
        for child in self.get_children():
            if child.is_leaf():
                leaf_name = child.get_name()
                file_path = dir_path + leaf_name + leaf_file_extension
                create_file(file_path)
            else:
                # Recurse into child composite
                # We assume child is a Composite that implements create_directory_structure.
                # If you have a formal interface, you can use isinstance checks instead.
                child.create_directory_structure(dir_path, leaf_file_extension)