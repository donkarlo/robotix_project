from robotix.mind.memory.long_term.explicit.episodic.experience.episode.episode import Episode
from typing import List, override

from robotix.mind.memory.long_term.explicit.episodic.experience.group.group import Group as ExperienceGroup
from robotix.mind.memory.trace.trace import Trace
from robotix.mind.memory.trace.observer.creation_subscriber import \
    CreationSubscriber


class Memorizing(CreationSubscriber):
    """
    - The _layers place will be detrmined
    """
    def __init__(self):
        #should be set by calling set _layers from Memory class
        self._experience_group = None

    def memorize(self, episodes:List[Episode])->None:
        """
        What entities exist to memorize

        """
        pass

    def set_experience_group(self, experience_group: ExperienceGroup) -> None:
        self._experience_group = experience_group


    @override
    def do_with_created_trace(self, trace: Trace) ->None:
        pass
