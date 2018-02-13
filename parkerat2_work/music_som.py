__author__ = 'parkerat2'

import sys
import random
import pandas as pd
import math
import operator
import scipy.spatial.distance as sd
import numpy as np
import matplotlib.pyplot as plt

args = sys.argv
n = 24
m = 12
p = 20
c = 20
y = 360
a = 0.02


def d(i, j, k, l):
    dik = abs(i - k)
    if dik > p / 2:
        dik = p - dik

    djl = abs(j - l)
    if djl > p / 2:
        djl = p - djl

    dis = math.sqrt(dik**2 + djl**2)
    return dis


def main():
    #args = sys.argv
    dfo = pd.read_csv(args[1])
    #dfo = pd.read_csv("chords.csv")
    df = dfo.drop('Label', axis=1)
    dfo = dfo.as_matrix()
    df = df.as_matrix()

    W = [[[random.uniform(0, 1) for k in range(m)] for j in range(p)] for i in range(p)]

    for s in range(1, y + 1):
        for t in range(1, n + 1):
            r = random.randrange(0, n)
            rt = df[r]
            mini = float("inf")
            mi = float("inf")
            mj = float("inf")
            for i in range(1, p + 1):
                for j in range(1, p + 1):
                    mn = sd.euclidean(W[i - 1][j - 1], rt)
                    if mn < mini:
                        mini = mn
                        mi = i
                        mj = j
            for k in range(1, p + 1):
                for l in range(1, p + 1):
                    o = 1/3 * (p - 1 - s / c)
                    O = math.e**(-(d(mi, mj, k, l)/(2 * o**2)))
                    z = list(map(operator.sub, rt, W[k - 1][l - 1]))
                    z = [O * a * x for x in z]
                    W[k - 1][l - 1] = list(map(operator.add, W[k - 1][l - 1], z))

    chords = [["" for j in range(p)] for i in range(p)]

    for i in range(0, p):
        for j in range(0, p):
            close = -1 * float("inf")
            index = float("inf")
            for k in range(len(df)):
                cl = 1 - sd.cosine(W[i][j], df[k])
                if cl > close:
                    close = cl
                    index = k
            chords[i][j] = dfo[index, 0]

    #figure 2
    CM = df[0]
    CMmap = np.zeros((p, p))
    for i in range(len(CMmap)):
        for j in range(len(CMmap[i])):
            CMmap[i][j] = np.dot(np.array(CM), np.array(W[i][j]))
    plt.figure()
    plt.imshow(CMmap, cmap='hot', interpolation='nearest')
    plt.gca().invert_yaxis()
    plt.gca().set_xticklabels(np.arange(0, 21, 1))
    plt.gca().set_yticklabels(np.arange(0, 21, 1))
    plt.gca().set_xticks(np.arange(-0.5, 20, 1))
    plt.gca().set_yticks(np.arange(-0.5, 20, 1))
    plt.gca().set_title("C Major Heatmap")
    plt.xlim(-0.5, 19.5)
    plt.ylim(-0.5, 19.5)
    plt.xlim(-0.5, 19.5)
    plt.ylim(-0.5, 19.5)
    plt.colorbar()
    plt.savefig(args[3])

    #figure 3
    Cm = df[12]
    Cmmap = np.zeros((p, p))
    for i in range(len(Cmmap)):
        for j in range(len(Cmmap[i])):
            Cmmap[i][j] = np.dot(Cm, W[i][j])
    plt.figure()
    plt.imshow(Cmmap, cmap='hot', interpolation='nearest')
    plt.gca().invert_yaxis()
    plt.gca().set_xticklabels(np.arange(0, 21, 1))
    plt.gca().set_yticklabels(np.arange(0, 21, 1))
    plt.gca().set_xticks(np.arange(-0.5, 20, 1))
    plt.gca().set_yticks(np.arange(-0.5, 20, 1))
    plt.gca().set_title("C minor Heatmap")
    plt.xlim(-0.5, 19.5)
    plt.ylim(-0.5, 19.5)
    plt.colorbar()
    plt.savefig(args[4])

    # figure 1
    plt.figure()
    for i in range(len(chords)):
        for j in range(len(chords[i])):
            if 'M' in chords[i][j]:
                plt.text(i, j, chords[i][j], ha='center', va='center', color='cyan')
            else:
                plt.text(i, j, chords[i][j], ha='center', va='center', color='pink')
    plt.xlim(-0.5, 19.5)
    plt.ylim(-0.5, 19.5)
    plt.gca().set_xticklabels(np.arange(0, 21, 1))
    plt.gca().set_yticklabels(np.arange(0, 21, 1))
    plt.gca().set_xticks(np.arange(-0.5, 20, 1))
    plt.gca().set_yticks(np.arange(-0.5, 20, 1))
    plt.gca().set_title("Circle of Fifths")
    plt.gca().set_xlabel("Major - Cyan | Minor - Pink")
    plt.xlim(-0.5, 19.5)
    plt.ylim(-0.5, 19.5)
    plt.gca().grid(which='major')
    plt.savefig(args[2])
    plt.show()
    plt.clf()

if __name__ == '__main__':
    main()
