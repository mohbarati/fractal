import colorsys
import itertools
import multiprocessing as mp
import os

import cv2
import numpy as np
from PIL import Image


def mandel(x, y):
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        else:
            c = c ** 2 + (x + 1j * y)
    return (0, 0, 0)


def rgb_conv(i):
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 155.0, 1.0, 0.5))
    return tuple(color.astype(int))


width = 2500 * 2
hight = 2000 * 2
a = np.linspace(-2, 0.5, width)
b = np.linspace(-1, 1, hight)
paramlist = list(itertools.product(a, b))


def func(params):
    x = params[0]
    y = params[1]
    return mandel(x, y)


if __name__ == "__main__":
    num_workers = mp.cpu_count()
    pool = mp.Pool(num_workers)
    results = pool.map(func, paramlist)
    image = np.array(results).reshape(width, hight, 3).astype(np.uint8)
    cv2.imwrite("img.png", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    os.system("shutdown -s")
