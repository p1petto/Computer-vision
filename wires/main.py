import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label


if __name__ == '__main__':
    count_of_files = 6
    for i in range(1, count_of_files+1):
        image = np.load(f"data/wires{i}.npy")
        struct = np.ones((3, 1))
        labeled = label(image)

        eroded = binary_erosion(image, struct) * 1
        wires = []
        d = {}

        for lb in range(1, labeled.max() + 1):
            t = np.zeros_like(image)
            t[labeled == lb] = 1
            wires.append(t)

        for a in range(len(wires)):
            d.update({a + 1: len(np.unique(label(binary_erosion(wires[a]) * 1))) - 1})

        print(d)

        # plt.imshow(label(image))
        # plt.show()
