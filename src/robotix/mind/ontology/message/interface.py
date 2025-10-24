from typing import Protocol

class Interface(Protocol):
    """
    - for example conversion from Tree(nested Dict) to TimedPoseDistribution
    -
    """
    sender: Messager
    def build_from_type(self, type:Type)->"Interface": ...
    def convert_to(self, type:Type)->"Interface": ...