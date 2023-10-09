import sys
import numpy as np


def list_data(data):
    data = [(line.strip()) for line in data]
    max_size_mm = int(data[0])
    data = data[2:]
    data = [list(map(int, line.strip().split())) for line in data[2:]]
    return max_size_mm, data


def get_points(data):
    # крайняя верхняя левая тока объекта
    min_horizontal = sys.maxsize
    min_vertical = sys.maxsize
    flag = False
    # max_horizontal = -sys.maxsize - 1
    for i in range(len(data)):
        if 1 in data[i]:
            if not flag:
                min_vertical = i
                flag = True
            for j in range(len(data[0])):
                if data[i][j] == 1:
                    if min_horizontal > j:
                        min_horizontal = j
                    break
    return [min_vertical, min_horizontal]


def get_offset(point1, point2):
    return point1 - point2


if __name__ == '__main__':
    with open("datas/img1.txt", 'r') as file:
        data1 = file.readlines()
    with open("datas/img2.txt", 'r') as file:
        data2 = file.readlines()

    max_size_mm1, data1 = list_data(data1)
    max_size_mm2, data2 = list_data(data2)

    p1 = np.array(get_points(data1))
    p2 = np.array(get_points(data2))

    print(get_offset(p2, p1))
