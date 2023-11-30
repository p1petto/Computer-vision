import numpy as np
from skimage.measure import label, regionprops
import cv2 as cv


def find_pencils(labeled_image, min_aspect_ratio=10):
    count_pencils = 0
    filtered_labeled = np.zeros_like(labeled_image)

    for region in regionprops(labeled_image):
        bbox = region.bbox

        if (region.axis_major_length / region.axis_minor_length) > min_aspect_ratio:
            count_pencils += 1
            filtered_labeled[bbox[0]:bbox[2], bbox[1]:bbox[3]] += region.image

    return filtered_labeled, count_pencils


if __name__ == '__main__':
    count_pencils = 0
    for i in range(1, 13):

        img = cv.imread(f"images/img ({i}).jpg", cv.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"
        ret, binary_image = cv.threshold(img, 142, 255, cv.THRESH_BINARY_INV)

        kernel = np.ones((3, 3), np.uint8)
        opened_image = cv.morphologyEx(
            binary_image, cv.MORPH_OPEN, kernel, iterations=2)
        closed_image = cv.morphologyEx(
            opened_image, cv.MORPH_CLOSE, kernel, iterations=2)

        labeled = label(closed_image)
        labeled = labeled[50:-50, 50:-50]

        # фильтрация маленьких объектов
        min_object_size = 100
        labeled = np.where(np.isin(labeled, [prop.label for prop in regionprops(labeled) if prop.area >= min_object_size]), labeled, 0)

        for region in regionprops(labeled):
            bbox = region.bbox
            r = labeled[bbox[0]:bbox[2], bbox[1]:bbox[3]]

        temp = find_pencils(labeled)
        filtered = temp[0]
        count_pencils += temp[1]


print(count_pencils)

