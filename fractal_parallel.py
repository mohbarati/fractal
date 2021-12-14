#!/usr/bin/env python3
import itertools
import multiprocessing

import numpy as np
from PIL import Image


def mandel(x, y):
    c = 0
    for _ in range(1, 200):
        if abs(c) > 2:
            return (0, 0, 0)
        else:
            c = c ** 2 + (x + 1j * y)
    return (100, 200, 150)


a = np.linspace(0, 1, img.size[0])
b = np.linspace(0, 0.5, img.size[1])
c = range(img.size[0])
d = range(img.size[1])
img = Image.new("RGB", (1920, 1080))
pixels = img.load()
for i, x in enumerate(a):
    for j, y in enumerate(b):
        pixels[i, j] = mandel(x, y)
img.show()

# Generate values for each parameter


# Generate a list of tuples where each tuple is a combination of parameters.
# The list will contain all possible combinations of parameters.
paramlist = list(itertools.product(a, b, c, d))

# A function which will process a tuple of parameters
def func(params):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    return a * b * c * d


# Generate processes equal to the number of cores
pool = multiprocessing.Pool()

# Distribute the parameter sets evenly across the cores
res = pool.map(func, paramlist)
