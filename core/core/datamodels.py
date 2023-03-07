import math
from dataclasses import dataclass


@dataclass
class CircleV0:
    x: float
    r: float

    @property
    def area(self) -> float:
        return math.pi * self.r * self.r
