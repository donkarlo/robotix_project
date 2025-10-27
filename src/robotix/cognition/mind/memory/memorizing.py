from typing import List
from robotix.cognition.mind.memory.episode.episode import Episode
from robotix.cognition.mind.memory.episode.experience_set import ExperienceSet


class Memorizing:
    """
    - The _levels place will be detrmined
    """
    def __init__(self):
        #should be set by calling set _levels from Memory class
        self._experience_set = None

    def memorize(self, episodes:List[Episode])->None:
        """
        What entities exist to memorize

        """
        pass

    def set_experience_set(self, experience_set:ExperienceSet) -> None:
        self._experience_set = experience_set

