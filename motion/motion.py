import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


if __name__ == '__main__':
    points = []
    x_first, y_first, x_second, y_second = [], [], [], []

    for i in range(100):
        image = np.load(f"out/h_{i}.npy")
        labeled = label(image)
        # filtered_labeled = np.zeros_like(labeled)

        regions = sorted(regionprops(label(image)), key=lambda region: region.area)

        # for region in detected_regions:
        #     bbox = region.bbox
        #     filtered_labeled[bbox[0]:bbox[2], bbox[1]:bbox[3]] += region.image
        #     print(region.centroid)

        (y1, x1) = regions[0].centroid
        (y2, x2) = regions[1].centroid

        x_first.append(x1)
        y_first.append(y1)
        x_second.append(x2)
        y_second.append(y2)

    plt.title("Object Trajectories")
    plt.plot(x_first, y_first, label='Object 1')
    plt.plot(x_second, y_second, label='Object 2')
    plt.legend()
    plt.show()

