import math

from core.datamodels import CircleV0


def test_circle_v0() -> None:
    circle = CircleV0(x=5, r=6)

    assert circle.area == math.pi * 6 * 6
