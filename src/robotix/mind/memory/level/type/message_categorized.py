from robotix.mind.memory.level.level import Level


class MessageCategorized(Level):
    def __init__(self):
        self._cats = []

    def add_message(self, message:Message):
        pass