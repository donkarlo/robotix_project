from robotix.mind.mind import Mind
from robotix.body.body import Body
from robotix.robot import Robot


class Human(Robot):
    def __init__(self, body:Body, mind:Mind):
        super().__init__(body, mind)

    def talk(self, message):
        pass