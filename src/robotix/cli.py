from utilix.ui.cli.cli import Cli as BaseCli
from robotix.experiment.experiment import Experiment


class Cli(BaseCli):
    def run(self):
        if self._args[0] == "xpr":
            pass
