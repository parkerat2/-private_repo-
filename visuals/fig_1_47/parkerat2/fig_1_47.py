import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

def main():
    args = sys.argv
    carsdf = pd.read_csv(args[1])
    # carsdf = pd.read_csv("cars04.csv")

    h = []
    c = []
    cy = set()
    for cmpg, hp, cyl, in zip(carsdf['City MPG'],
                carsdf['HP'], carsdf['Cyl']):
        if hp is not '*' and cmpg is not '*' and cyl is not -1:
            h.append(int(hp))
            c.append(int(cmpg))
            cy.add(cyl)
            hp=float(hp)
            cmpg=float(cmpg)
            cyl=float(cyl)
            if cyl == 3:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='y', edgecolors='gray', label=3)
            if cyl == 4:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='g', edgecolors='gray', label=4)
            if cyl == 5:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='m', edgecolors='gray', label=5)
            if cyl == 6:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='k', edgecolors='gray', label=6)
            if cyl == 8:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='c', edgecolors='gray', label=8)
            if cyl == 10:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='gray', edgecolors='gray', label=10)
            if cyl == 12:
                plt.scatter(x=hp, y=cmpg, marker='s', s=(cyl * 15), color='r', edgecolors='gray', label=12)

    plt.xticks(np.arange(min(h), max(h) + 10, 42.7))
    plt.yticks(np.arange(min(c), max(c)+1, 5))
    plt.xlim(xmin=min(h)-5, xmax=max(h)+13)
    plt.ylim(ymin=min(c)-2, ymax=max(c)+2)
    plt.xlabel("HP")
    plt.ylabel("City MPG")
    plt.title("2004 Vehicle Comparison of Horsepower, City MPG, and # of Cylinders")
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), title="# Cylinders")
    # plt.show()
    plt.savefig(sys.argv[2])
    plt.clf()


if __name__ == '__main__':
    main()
