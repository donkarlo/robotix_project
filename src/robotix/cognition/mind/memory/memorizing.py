from robotix.cognition.mind.memory.long_term.explicit.episodic.episode.episode import Episode
from typing import List
from robotix.cognition.mind.memory.long_term.explicit.episodic.experience.collection.collection import Collection


class Memorizing:
    """
    - The _levels place will be detrmined
    """
    def __init__(self):
        #should be set by calling set _levels from Memory class
        self._experience_collection = None

    def memorize(self, episodes:List[Episode])->None:
        """
        What entities exist to memorize

        """
        pass

    def set_experience_collection(self, experience_collection:Collection) -> None:
        self._experience_collection = experience_collection

