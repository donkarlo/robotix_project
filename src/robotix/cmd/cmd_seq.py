from robotix.cmd.cmd import Cmd


class CmdSeq:
    def __init__(self, cmd_sq:list[Cmd,...]):
        self._cmd_sq = cmd_sq


