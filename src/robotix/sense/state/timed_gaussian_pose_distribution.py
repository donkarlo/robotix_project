from mathx.probability.covariance_matrix import CovarianceMatrix
from mathx.probability.distribution.gaussian.distribution import Distribution
from physix.dimension.unit.scalar import Scalar
from physix.kinematics.pose import Pose


class TimedGaussianPoseDistribution(Distribution):
    def __init__(self, time:Scalar , mu:Pose, cov:CovarianceMatrix):
        super().__init__(mu, cov)
        self._time = time