import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label


def count_of_figures(image, mask):
    eroded = label(binary_erosion(image, mask))
    return len(np.unique(eroded)) - 1


if __name__ == '__main__':
    mask1 = np.array([[0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0],
                      [1, 1, 1, 1, 1],
                      [0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0]])

    mask2 = np.array([[1, 0, 0, 0, 1],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [1, 0, 0, 0, 1]])

    image = np.load(f"data/stars.npy")
    labeled = label(image)

    count_of_plus = count_of_figures(image, mask1)
    count_of_cross = count_of_figures(image, mask2)
    print(count_of_cross+count_of_plus)
