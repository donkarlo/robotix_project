from typing import Protocol, List

from robotix.mind.memory.remembering.observer.remeber_episode_subscriber import RememberEpisodeSubscriber


class RemeberEpisodePublisher(Protocol):
    _remeber_episode_subscribers:List[RememberEpisodeSubscriber]
    def attach_remeber_episode_subscriber(self, remeber_episode_subscriber:RememberEpisodeSubscriber)->None: ...
    def detach_remeber_episode_subscriber(self, remeber_episode_subscriber: RememberEpisodeSubscriber)->None: ...
    def notify_remeber_episode_subscribers(self)->None: ...
