from robotix.cognition.mind.memory.long_term.ecplicit.level.level import Level


class MessageCategorized(Level):
    def __init__(self):
        self._cats = []

    def add_message(self, message:Message):
        pass