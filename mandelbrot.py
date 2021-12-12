import matplotlib.pyplot as plt
import numpy as np

cx = np.arange(-1, 1, 0.01)
cy = np.arange(-1, 1, 0.01)

xx, yy = np.meshgrid(cx, cy)
for i, j in zip(*np.vstack([xx.ravel(), yy.ravel()])):
    print(i, j)


# plt.plot(xx, yy, marker=".", color="k", linestyle="none")
# plt.show()
