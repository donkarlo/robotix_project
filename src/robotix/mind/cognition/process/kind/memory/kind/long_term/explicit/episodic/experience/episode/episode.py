from robotix.trace.trace import Trace


class  Episode:
    """
    Maybe different from Force, I should think about it
    - from what an episodic must be composed
        − Mission
        − pre_plan
        - mind world is formed by experoceptive
    """
    def __init__(self, traces:list[Trace]):
        """

        Args:
            traces: we need a group of traces so large to get the information what-where-when-who
        """
        self._trace = traces

    def get_traces(self):
        return self._trace
