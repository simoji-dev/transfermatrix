import pandera as pa
from pandera.typing import Series
from enum import Enum


class Layer(pa.SchemaModel):

    wavelengths: Series[float] = pa.Field(coerce=True)      # wavelengths in nm
    nk: Series[float] = pa.Field(coerce=True)               # complex refractive index


class CoherentLayer(Layer):

    thickness: float = pa.Field(coerce=True)                # layer thickness in nm


class Polarization(str, Enum):
    P = "p"
    S = "s"
