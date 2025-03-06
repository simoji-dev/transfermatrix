import dataclasses
import pydantic
from enum import Enum
from pathlib import Path
from typing import Callable, Optional


@dataclasses.dataclass
class OpticalConstants:
    """Wavelengths-dependent optical constants of a material."""

    wavelengths: list[float]    # wavelengths in nm
    n: list[float]              # refractive index (real part)
    k: list[float]              # extinction coefficient


@dataclasses.dataclass
class Layer:
    """Two-dimensional layer of an optical layer stack."""

    optical_constants: OpticalConstants
    thickness: float | int | None
    is_coherent: bool = False

    def __post_init__(self):
        assert (isinstance(self.thickness, float | int) or ((self.thickness is None) and (not self.is_coherent)))


class Polarization(str, Enum):
    P = "p"
    S = "s"
