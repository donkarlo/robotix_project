from typing import Protocol

from robotix.mind.memory.long_term.explicit.episodic.episode.episode import Episode


class RememberEpisodeSubscriber(Protocol):
    def do_with_remebered_episode(self, episode: Episode) -> None: ...