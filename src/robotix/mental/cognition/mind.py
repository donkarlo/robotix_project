from robotix.mental.cognition.decision_making.decision_making import DecisionMaking
from robotix.mental.cognition.learning.learning import Learning
from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace import Trace
from robotix.mental.cognition.memory.long_term.explicit.episodic.trace.trace_arrival_observer_interface import \
    TraceArrivalObserverInterface
from robotix.mental.cognition.memory.memory import Memory
from typing import override

from robotix.mental.cognition.reasoning.reasoning import Reasoning


class Mind(TraceArrivalObserverInterface):
    """
    Is all about the concepts. Whenever there is something tangiable, it should go to physical>brain
    - https://en.wikipedia.org/wiki/Mind
        - The mind is that which thinks, feels, perceives, imagines, remembers, and wills. It covers the totality of mental phenomena, including both conscious processes, through which an individual is aware of external and internal circumstances, and unconscious processes, which can influence an individual without intention or awareness.
    """
    def __init__(self, memory:Memory, learning:Learning, reasoning:Reasoning, decision_making:DecisionMaking):
        """

        Args:
            memory:
            learning: learning strategy, updating model parametes
            reasoning: reasoning strategy, how to relate new observations using learning strategy (the parameters from learning)
            decision_making: selection of a belief among several possible alternative options
        """
        self._memory = memory
        self._reasoning = reasoning
        self._learning = learning
        self._decision_making = decision_making


    def get_learning(self)->Learning:
        return self._learning

    def get_reasoning(self)->Reasoning:
        return self._reasoning

    def get_decision_making(self)->DecisionMaking:
        return self._decision_making

    def get_memory(self)->Memory:
        return self._memory

    @override
    def do_with_arrived_trace(self, trace: Trace) ->None:
        self.get_memory().do_with_arrived_trace(trace)
