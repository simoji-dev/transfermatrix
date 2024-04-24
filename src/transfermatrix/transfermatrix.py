from typing import Sequence, Optional
from input import Layer, Polarization


class TransferMatrix:
    """
    Calculate transfer matrix and resulting quantities (R, T, A, Psi, Delta) of layer stack with coherent and incoherent
    layers. Light propagation direction is always from first to last layer.
    """

    def __init__(self,
                 layers: Sequence[Layer],
                 polarization: Polarization,
                 wavelengths: Sequence[float]
                 ):
        pass
        # todo:
        # map layer nk to wavelengths

    def calculate_for_angles(self,
                             angles_deg: Sequence[float],
                             layer_index_angle_definition: Optional[int] = 0,
                             selected_layers_indices: Optional[Sequence[int]] = None):
        pass
        # todo:
        # convert angles to wave vectors
        # calculate kz_3d [layer, wavelengths, wave vectors]
        # translate in incoherent stack, coherent sub-stacks are like interfaces

    def calculate_for_wave_vectors(self,
                                   normalized_in_plane_wave_vectors: Sequence[float],
                                   layer_index_angle_definition: Optional[int] = 0,
                                   selected_layers_indices: Optional[Sequence[int]] = None):
        pass
        # todo:
        # calculate kz_3d [layer, wavelengths, wave_vectors]
        # translate in incoherent stack, coherent sub-stacks are like interfaces


class TransferMatrixCoherent:
    """ Calculate the transfer matrix of a coherent layer stack."""

    def __init__(self):
        pass
