from typing import Protocol, runtime_checkable

from physix.quantity.quantifiable import Quantifiable


@runtime_checkable
class Interface(Quantifiable, Protocol): ...
