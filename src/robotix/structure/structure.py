from functools import cache
from pathlib import Path

from utilix.data.kind.dic.dic import Dic
from utilix.data.storage.kind.file.yaml.yaml import Yaml as YamlStorage
from utilix.os.file_system.file.file import File as OsFile
from utilix.os.file_system.path.file import File as FilePath


class Structure:
    """
    TODO: This structure must be made of composite pattern
    """
    def __init__(self):
        self._schema = None

    def get_structure(self) -> Dic:
        if self._schema is None:
            # it is in current folder
            current_dir_path = FilePath(__file__).get_containing_abolute_directory_path()
            current_file_path = current_dir_path + "structure.yaml"
            yaml_os_file = OsFile(FilePath(current_file_path), None, None)
            yaml = YamlStorage(yaml_os_file, None)
            self._schema = yaml.get_ram()
        return self._schema

    def draw(self):
        self.get_structure().draw()


if __name__ == "__main__":
    schema = Structure().draw()
