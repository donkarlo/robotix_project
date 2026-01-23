from dataclasses import dataclass

from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.large_language_model_example import \
    Chunk


@dataclass(frozen=True)
class RetrievalHit:
    score: float
    chunk: Chunk