from typing import List

from robotix.mind.cognition.semiotic.meaning.meaning import Meaning
from robotix.mind.cognition.semiotic.meaning.observation.formation_subcriber import FormationSubscriber


class FormationPublisher:
    _meaning_formation_subscribers: List[FormationSubscriber]
    def attach_meaning_formation_subscriber(self, formation_subscriber:FormationSubscriber)->None: ...
    def detach_meaning_formation_subscriber(self, formation_subscriber: FormationSubscriber)->None: ...
    def notify_meaning_formation_subscribers(self, meaning:Meaning)->None: ...