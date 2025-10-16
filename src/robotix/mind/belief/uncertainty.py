from mathx.numbers.real.interval.closed_unit_interval import ClosedUnitInterval


class Uncetainty(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_uncertainty_rate(self) -> ClosedUnitInterval:
        """Just to assign a value"""
        pass
