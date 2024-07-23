from transfermatrix.input import Layer

wl = [100, 200, 300]
n = [1.1, 1.2, 1.3]
k = [0, 0, 0]

layer = Layer(wavelengths=wl, n=n, k=k)

print(layer)
