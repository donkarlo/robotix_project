# -----------------------------
# AppFactory (OOP)
# -----------------------------
from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.rag.answer_policy import \
    AnswerPolicy
from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.rag.rag_engine import \
    RagEngine
from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.rag.runtime_config import \
    RuntimeConfig
from robotix.structure.kind.mind.cognition.semiotic.language.natural.large_language_model.rag.terminal_app import \
    TerminalApp


class AppFactory:
    def __init__(self, cfg: RuntimeConfig, policy: AnswerPolicy):
        self._cfg = cfg
        self._policy = policy

    def build(self) -> TerminalApp:
        rag = RagEngine(cfg=self._cfg, policy=self._policy)
        return TerminalApp(rag=rag)