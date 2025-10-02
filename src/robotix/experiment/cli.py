from typing import Optional, List

from utilix.ui.cli.cli import Cli as BaseCli

class Cli(BaseCli):
    def __init__(self, faked_argv: Optional[List[str]]=None):
        super().__init__(faked_argv)
        self._type = self._args[1] # such as oldest
        self._command = self._args[2] # such as learn

    def get_type(self):
        return self._type

    def get_command(self):
        return self._command