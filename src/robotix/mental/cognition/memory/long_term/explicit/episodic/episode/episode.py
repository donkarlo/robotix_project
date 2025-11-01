from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace import Trace


class  Episode:
    """
    Maybe different from Trigger, I should think about it
    - from what an episodic must be composed
        − Mission
        − pre_plan
        - mental world is formed by experoceptive
    """
    def __init__(self, traces:list[Trace]):
        self._trace = traces

    def get_traces(self):
        return self._trace
