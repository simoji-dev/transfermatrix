import pydantic
from enum import Enum


class Layer(pydantic.BaseModel):

    wavelengths: list[float]        # wavelengths in nm
    n: list[float]                  # refractive index (real part)
    k: list[float]                  # extinction coefficient


class CoherentLayer(Layer):

    thickness: float                # layer thickness in nm


class Polarization(str, Enum):
    P = "p"
    S = "s"
