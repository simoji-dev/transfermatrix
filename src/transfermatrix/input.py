import pydantic
from enum import Enum
from pathlib import Path
from typing import Callable, Optional


class OpticalConstants(pydantic.BaseModel):

    wavelengths: list[float]    # wavelengths in nm
    n: list[float]              # refractive index (real part)
    k: list[float]              # extinction coefficient


class Layer:

    def __init__(self, nk_file: Path, nk_reader: Callable[[Path], OpticalConstants], thickness: Optional[float] = None,
                 is_coherent: Optional[bool] = False):

        optical_constants: OpticalConstants = nk_reader(nk_file)

        self.wavelengths = optical_constants.wavelengths
        self.n = optical_constants.n
        self.k = optical_constants.k

        self.thickness: float | None = thickness
        self.is_coherent: bool = is_coherent

        assert (isinstance(self.thickness, float) or ((self.thickness is None) and (not self.is_coherent)))


class Polarization(str, Enum):
    P = "p"
    S = "s"
