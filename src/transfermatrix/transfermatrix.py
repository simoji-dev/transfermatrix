import transfermatrix.interfaces


class TransferMatrix:
    """
    Calculate transfer matrix and resulting quantities (R, T, A, Psi, Delta) of layer stack with coherent and incoherent
    layers. Light propagation direction is always from first to last layer.
    """

    def __init__(self, layer_stack: transfermatrix.interfaces.LayerStack):
        self.layer_stack = layer_stack

    def __call__(self, config: transfermatrix.interfaces.Configuration):
        pass
        # todo:
        # calculate kz_3d [layer, wavelengths, wave_vectors]
        # translate in incoherent stack, coherent sub-stacks are like interfaces


class TransferMatrixCoherent:
    """ Calculate the transfer matrix of a coherent layer stack."""

    def __init__(self):
        pass
