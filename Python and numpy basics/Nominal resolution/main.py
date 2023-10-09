import sys

if __name__ == '__main__':
    files = [1, 2, 4, 5, 6]
    for num in files:
        with open(f"datas/figure{num}.txt", 'r') as file:
            data = file.readlines()

        data = [(line.strip()) for line in data]
        max_size_mm = int(data[0])
        data = data[2:]
        data = [list(map(int, line.strip().split())) for line in data[2:]]

        min_horizontal = sys.maxsize
        max_horizontal = -sys.maxsize - 1

        for i in range(len(data)):
            if 1 in data[i]:
                for j in range(len(data[0])):
                    if data[i][j] == 1:
                        if min_horizontal > j:
                            min_horizontal = j
                        break
                for k in range(len(data[0])-1, -1, -1):
                    if data[i][k] == 1:
                        if max_horizontal < k:
                            max_horizontal = k
                        break

        if min_horizontal == sys.maxsize or max_horizontal == -sys.maxsize - 1:
            nominal_size = 0
        else:
            width_px = max_horizontal - min_horizontal + 1
            nominal_size = max_size_mm/width_px

        print(f"figure{num}: {nominal_size}")

