from physix.dimension.unit.scalar import Scalar
from physix.dimension.unit.vec import Vec as UnitedVec
from robotix.structure.kind.body.sensor.observation.observation import Observation


class Factory:
    @staticmethod
    def get_timed_obs(united_val: UnitedVec, united_time:Scalar)->Interface:
        return Timed(Observation(united_val, united_time))

