from typing import List
from robotix.mind.memory.episode.episode import Episode
from robotix.mind.memory.level.levels import Levels


class Memorizing:
    """
    - The levels place will be detrmined
    """
    def __init__(self):
        #should be set by calling set levels from Memory class
        self._levels = None

    def memorize(self, episodes:List[Episode])->bool:
        """
        What entities exist to memorize

        """
        return False

    def set_levels(self, levels: Levels) -> None:
        self._levels = levels

