import numpy as np
import matplotlib.pylab as plt
import sys

from sklearn import decomposition


def results(file_name):
    data = np.empty((0, 4), float)
    file = open(file_name, 'r')
    line_cnt = 0
    min_data = [100 for i in range(0, 4)]
    max_data = [-100 for i in range(0, 4)]
    list = []

    for line in file:
        if line_cnt == 0:
            line_cnt += 1
            continue
        l = line.split(',')
        b = [float(l[i]) for i in range(0, 4)]
        list.append(b)

        for i in range(0, 4):
            if b[i] < min_data[i]:
                min_data[i] = b[i]
            if b[i] > max_data[i]:
                max_data[i] = b[i]

        data = np.append(data, np.array([b]), axis=0)

    pca = decomposition.PCA(n_components=4)
    pca.fit(data)
    x = pca.transform(data)

    scale = [0.22, 0.05]
    # print(max_data)
    # print(min_data)
    for e in range(len(list)):
        for i in range(0, 4):
            list[e][i] = (list[e][i] - min_data[i]) / (max_data[i] - min_data[i]) * scale[i % 2]

        # print(list[e])

    plot(x, list)


def plot(x, data):
    plt.title('Iris star glyphs')

    d1 = []
    d2 = []
    for i in x:
        d1.append(i[0]*-1)
        d2.append(i[2]*-1)

    for i in range(0, len(d1)):
        drawStar(d1[i], d2[i], data[i])

    plt.xlabel('PC2')
    plt.ylabel('PC1')

    # plt.show()
    plt.savefig(sys.argv[2])
    return


def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], color='green', linewidth=0.3)


def drawStar(px, py, data):
    lx = []
    ly = []

    # x changed y unchanged
    lx.append(px + data[0])
    ly.append(py)

    ly.append(py + data[1])
    lx.append(px)

    # x changed y unchanged
    lx.append(px - data[2])
    ly.append(py)

    ly.append(py - data[3])
    lx.append(px)

    plt.plot(lx, ly, color='green', linewidth=0.3)
    for i in range(0, len(lx)):
        for j in range(i + 1, len(lx)):
            connectpoints(lx, ly, i, j)


if __name__ == '__main__':
    if sys.argv == 1:
        print('Accept one argument: No input file for data')
        exit(0)

    results(sys.argv[1])

