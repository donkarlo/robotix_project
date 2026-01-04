from robotix.body.body import Body
from robotix.mind.mind import Mind
from utilix.os.file_system.path.directory import Directory
from abc import ABC, abstractmethod
from typing import Optional

class Factory(ABC):
    def __init__(self, name:str):
        """

        Args:
            root_directory: must contain both mind tree and body tree
        """
        self._mind:Optional[Mind] = None
        self._body:Optional[Body] = None
    def init_from_directory(self):
        # TODO: a folder that should have the mind>memory body>sensors etc
        pass

    @abstractmethod
    def build(self):
        # TODO: do not allow to build unless mind and body are ready
        pass