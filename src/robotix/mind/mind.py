from robotix.mind.cognition.semiotic.meaning.observation.fomation_publisher import FormationPublisher as MeaningFormationPublisher
from robotix.mind.cognition.semiotic.meaning.observation.formation_subcriber import FormationSubscriber as MeaningFormationSubscriber
from robotix.mind.decision_making.decision_making import DecisionMaking
from robotix.mind.learning.learning import Learning
from robotix.mind.memory.working import Working
from typing import List
from robotix.mind.reasoning.reasoning import Reasoning


class Mind(MeaningFormationPublisher):
    """
    Mental is the adverb for mind
    https: // en.wikipedia.org / wiki / Mental_model
        - A mind model is an internal representation of external reality — that is, a way of representing reality within the mind.

    Is all about the concepts. Whenever there is something tangiable, it should go to body>brain
    - https://en.wikipedia.org/wiki/Mind
        - The mind is that which thinks, feels, perceives, imagines, remembers, and wills. It covers the totality of mind phenomena, including both conscious processes, through which an individual is aware of external and internal circumstances, and unconscious processes, which can influence an individual without intention or awareness.
    """
    def __init__(self, memory:Working, learning:Learning, reasoning:Reasoning, decision_making:DecisionMaking):
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

        self._meaning_formation_subscribers: List[MeaningFormationSubscriber] = []


    def get_learning(self)->Learning:
        return self._learning

    def get_reasoning(self)->Reasoning:
        return self._reasoning

    def get_decision_making(self)->DecisionMaking:
        return self._decision_making

    def get_memory(self)->Working:
        return self._memory






