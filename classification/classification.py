import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import numpy as np
from skimage import draw
from skimage.filters import gaussian
from skimage.measure import label, regionprops


def has_vline(arr):
    return 1. in arr.mean(0)


def recognize(prop):
    euler_number = prop.euler_number
    if euler_number == -1:  # две дырки 8 или B
        if has_vline(prop.image):
            return "B"
        else:
            return "8"
    elif euler_number == 0:  # одна дырка A 0 P D
        if has_vline(prop.image): # P D
            print(prop.eccentricity)
            if prop.eccentricity > 0.6:
                return "P"
            else:
                return "D"
        else:
            y, x = prop.centroid_local
            y /= prop.image.shape[0]
            x /= prop.image.shape[1]
            if np.isclose(x, y, 0.04):
                return "0"
            else:
                return "A"
    elif euler_number == 1:  # нет дырок 1 W X * - /
        if prop.image.mean() == 1.0:
            return "-"
        else:
            if has_vline(prop.image) and has_vline(prop.image.T):
                return "1"
            else:
                tmp = prop.image.copy()
                tmp[[0, -1], :] = 1
                tmp[:, [0, -1]] = 1
                tmp_labeled = label(tmp)
                tmp_props = regionprops(tmp_labeled)
                tmp_euler = tmp_props[0].euler_number
                if tmp_euler == -3:
                    return "X"
                elif tmp_euler == -1:
                    return "/"
                else:
                    if prop.eccentricity > 0.5:
                        return "W"
                    else:
                        return "*"

    return "_"


if __name__ == '__main__':
    image = plt.imread(r"symbols.png")
    # image = plt.imread(r"alphabet-ext.png")
    image = image.mean(2)

    binary = image > 0
    labeled = label(binary)
    print(np.max(labeled))

    props = regionprops(labeled)

    # euler_number -1 - две дырки, 0 - одна дырка, 1 - нет дырок

    result = {}
    for prop in props:
        symbol = recognize(prop)
        if symbol not in result:
            result[symbol] = 0
        result[symbol] += 1
    print(result)
    print((1 - result.get("_", 0) / np.max(labeled)) * 100)

    plt.imshow(labeled)
    plt.show()
