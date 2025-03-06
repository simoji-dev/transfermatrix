from transfermatrix.interfaces import Layer, OpticalConstants

wl = [100, 200, 300]
n = [1.1, 1.2, 1.3]
k = [0, 0, 0]

optical_constants = OpticalConstants(wavelengths=wl, n=n, k=k)
layer = Layer(optical_constants, thickness=10.)

print(layer)
