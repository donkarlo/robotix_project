from robotix.structure.kind.mind.ontology.message.messageable import Messageable
from mathx.probability.distribution.gaussian.distribution import Distribution


class GaussianPoseDestribution(Distribution, Messageable):
    def __init__(self, pose:Pose):
        pass