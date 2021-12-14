import numpy as np
from PIL import Image


def mandel(x, y):
    c = 0
    for _ in range(1, 1000):
        if abs(c) > 2:
            return (0, 0, 0)
        else:
            c = c ** 2 + (x + 1j * y)
    return (100, 200, 150)


img = Image.new("RGB", (1800, 1200))
pixels = img.load()
for i, x in enumerate(np.linspace(0, 1, img.size[0])):
    for j, y in enumerate(np.linspace(0, 0.5, img.size[1])):
        pixels[i, j] = mandel(x, y)
img.show()
