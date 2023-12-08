import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops
from skimage.color import rgb2hsv

def group_colors(color):
    result = []
    while color:
        color1 = color.pop(0)
        result.append([color1])
        for color2 in color.copy():
            if abs(color1[0] - color2[0]) < 0.1:
                result[-1].append(color2)
                color.pop(color.index(color2))
    return result


if __name__ == '__main__':
    image = plt.imread("balls_and_rects.png")
    labeled = label(image.mean(2) > 0)
    hsv = rgb2hsv(image)
    rects = []
    circles = []


    print("Всего фигур: ", np.max(labeled))

    h = hsv[:, :, 0]
    colors = []
    for region in regionprops(labeled):
        bbox = region.bbox

        r = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]

        if len(np.unique(r)) == 1:
            rects.append((np.unique(r)[0], bbox))
            plt.show()
        else:
            circles.extend([(np.unique(r)[1], bbox)])


    print(f"Общее количество прямоугольников: {len(rects)}")
    print(f"Общее количество кругов: {len(circles)}")

    group_circles = group_colors(circles)
    group_rects = group_colors(rects)

    for group in group_circles:
        print(f"Оттенок: {group[0][0]}, Количество кругов: {len(group)}")

    for group in group_rects:
        print(f"Оттенок: {group[0][0]}, Количество квадратов: {len(group)}")



