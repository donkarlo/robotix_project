from abc import ABC, abstractmethod

class Cmd(ABC):
    '''a cmd that is sent to a robot to do something, maybe achieve a goal'''
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass