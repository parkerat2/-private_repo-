__author__ = 'Naibin Zheng'
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
from PIL import Image
import sys

def main():

    #iris = datasets.load_iris()
    iris = pd.read_csv(sys.argv[1])
    sl = iris['sepal length']/40
    sw = iris['sepal width']/40
    pl = iris['petal length']/40
    pw = iris['petal width']/40
    #print (sl)
    x = iris.as_matrix(columns=iris.columns[0:4])
    #print (x)

    m = x.mean(axis=0)
    #print (m)

    for i in range (len(x)):
        for j in range (len(x[i])):
            x[i][j] -= m[j]


    #print (x)


    pca = PCA(n_components=4)
    p = pca.fit_transform(x)
    #print (p)
    #print (pca.explained_variance_ratio_)
    #print (p[:, 0])
    fig =plt.figure()

    m = []
    n = []

    for x, y, sle, swi, ple, pwi in zip(p[:, 0], p[:, 2], sl, sw, pl, pw):

        #plt.scatter(-x, -y)
        #print (x)
        #print (y)
        x = - (x)
        #y = - (y)
        sle = -(sle)
        #swi = - (swi)
        ple = - (ple)
        #pwi = - (pwi)
        m.append(x+ple)
        m.append(x)
        m.append(x-sle)
        m.append(x)
        m.append(x+ple)
        m.append(x)
        m.append(x)
        m.append(x)
        m.append(x-sle)
        m.append(x)
        n.append(y)
        n.append(y)
        n.append(y)
        n.append(y+swi)
        n.append(y)
        n.append(y-pwi)
        n.append(y)
        n.append(y+swi)
        n.append(y)
        n.append(y-pwi)
        plt.plot(m, n, 'g')
        del m[:]
        del n[:]

    #plt.legend()
    plt.title('PCA of IRIS dataset')
    plt.xlabel('sepal length')
    plt.ylabel('petal length')


    #a=[-1, -1]
    #b=[-1, 1]
    #c=[1, 1]
    #d=[1, -1]
    #x=[a[0], b[0], c[0], d[0], a[0]]
    #y=[a[1], b[1], c[1], d[1], a[1]]
    #plt.plot(x, y)


    plt.show()
    fig.savefig(sys.argv[2])



if __name__ == '__main__':
    main()
