import dataclasses
import enum
import typing

import numpy as np


@dataclasses.dataclass
class OpticalConstants:
    """Wavelengths-dependent optical constants of a material."""

    wavelengths: typing.Sequence[float]    # wavelengths in nm
    n: typing.Sequence[float]              # refractive index (real part)
    k: typing.Sequence[float]              # extinction coefficient

    def __post_init__(self):
        assert len(self.wavelengths) == len(self.n)
        assert len(self.wavelengths) == len(self.k)

    def get_complex_refractive_index(self, wavelengths: typing.Union[typing.Sequence[float], None] = None) -> list[complex]:
        """Linear interpolate optical constants to given wavelengths."""

        if wavelengths is None:
            wavelengths = self.wavelengths

        assert min(wavelengths) >= min(self.wavelengths)
        assert max(wavelengths) <= max(self.wavelengths)

        n = np.interp(wavelengths, xp=self.wavelengths, fp=self.n)
        k = np.interp(wavelengths, xp=self.wavelengths, fp=self.k)

        return n + 1.j * k


@dataclasses.dataclass
class Layer:
    """Two-dimensional layer of an optical layer stack."""

    optical_constants: OpticalConstants
    thickness: float | int | None
    is_coherent: bool = False

    def __post_init__(self):
        assert (isinstance(self.thickness, float | int) or ((self.thickness is None) and (not self.is_coherent)))


@dataclasses.dataclass
class LayerStack:
    layers: typing.Sequence[Layer]

    def get_layers(self, indices) -> list[Layer]:
        return [self.layers[index] for index in indices]


class Polarization(str, enum.Enum):
    P = "p"
    S = "s"


class AngularType(str, enum.Enum):
    WAVE_VECTOR = "normalized in-plane wave-vector"
    ANGLE_DEG = "angle in degree"
    ANGLE_RAD = "angle in radiant"


class AngleConfig:
    """Angular """
    type: AngularType = AngularType.ANGLE_DEG
    layer_index: int | None = 0


@dataclasses.dataclass
class Configuration:
    polarization: Polarization
    wavelengths: typing.Sequence[float]
    angle_values: typing.Sequence[float]
    angle_config: AngleConfig
    selected_layers: typing.Sequence[int] | None = None
