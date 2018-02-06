__author__ = 'Naibin Zheng'
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib.patches import Rectangle
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    hp = data['HP']
    mpg = data['City MPG']
    weight = data['Weight']
    sedan = data['Small/Sporty/ Compact/Large Sedan']
    sc = data['Sports Car']
    suv = data['SUV']
    wagon = data['Wagon']
    minivan = data['Minivan']
    pickup=data['Pickup']


    #print(type)

    plt.xlabel('HP')
    plt.ylabel('City MPG')
    plt.title('The correlation between HP and City MPG in the different Size and Type of car')

    #for h, m, w, s, su, w, m, p in zip(hp, mpg, weight, sc, suv, wagon, minivan, pickup):
    for h, m, w, sd, s, su, wg, mv, p in zip(hp, mpg, weight, sedan, sc, suv, wagon, minivan, pickup):
        if h != '*' and m != '*' and w != '*' and sd == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='g')
        elif h != '*' and m != '*' and w != '*' and s == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='cyan')
        elif h != '*' and m != '*' and w != '*' and su == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='blue')
        elif h != '*' and m != '*' and w != '*' and p == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='y')
        elif h != '*' and m != '*' and w != '*' and wg == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='r')
        elif h != '*' and m != '*' and w != '*' and mv == 1:
            area = float(w)/25
            h = float(h)
            m = float(m)
            plt.scatter(h, m, marker='s', s=area, c='black')

    #plt.show()
    plt.savefig(sys.argv[2])


if __name__ == '__main__':
    main()
