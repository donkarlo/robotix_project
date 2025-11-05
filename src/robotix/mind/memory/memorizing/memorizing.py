from robotix.mind.memory.long_term.explicit.episodic.episode.episode import Episode
from typing import List
from robotix.mind.memory.long_term.explicit.experience.collection.collection import Collection
from robotix.mind.memory.long_term.explicit.episodic.trace.trace import Trace
from robotix.mind.memory.long_term.explicit.episodic.trace.observer.arrival_subscriber import \
    ArrivalSubscriber


class Memorizing(ArrivalSubscriber):
    """
    - The _layers place will be detrmined
    """
    def __init__(self):
        #should be set by calling set _layers from Memory class
        self._experience_collection = None

    def memorize(self, episodes:List[Episode])->None:
        """
        What entities exist to memorize

        """
        pass

    def set_experience_collection(self, experience_collection:Collection) -> None:
        self._experience_collection = experience_collection

    @override
    def do_with_arrived_trace(self, trace: Trace) -> None:
        pass

