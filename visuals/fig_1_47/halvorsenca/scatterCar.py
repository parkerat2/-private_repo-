import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import sys

file = sys.argv[1]
data = pd.read_csv(file)

details= pd.DataFrame(data, columns=['Vehicle Name', 'Small/Sporty/ Compact/Large Sedan','Sports Car', 'SUV', 'Wagon', 'Minivan', 'Pickup', 'AWD', 'RWD', 'Retail Price', 'Dealer Cost', 'Engine Size (l)', 'Cyl', 'HP', 'City MPG', 'Hwy MPG', 'Weight', 'Wheel Base', 'Len', 'Width'])

HP = list(details['HP'])
MPG = list(details['City MPG'])
WEIGHT = details['Weight']


temp = []
for m in MPG:
    if m == '*':
        temp.append(0)
    else:
        temp.append(float(m))

MPG = temp

temp2 = []
for w in WEIGHT:
    if w == '*':
        temp2.append(0)
    else:
        temp2.append(float(w))

WEIGHT=temp2

type={}

types = pd.DataFrame(data, columns=['Small/Sporty/ Compact/Large Sedan', 'Sports Car', 'SUV', 'Wagon', 'Minivan', 'Pickup'])
cars = pd.DataFrame(types).to_dict()

for c in cars:
    for i in cars[c]:
        if cars[c][i] == 1:
            type[i] = c
            
color_dict = {'Small/Sporty/ Compact/Large Sedan': 'red', 'Sports Car': 'blue', 'SUV': 'green', 'Wagon': 'purple', 'Minivan': 'black', 'Pickup':'cyan'}

colors = {}
for every in type:
    colors[every] = color_dict[type[every]]

color_list = []
for i in range(len(colors)):
    color_list.append(colors[i])

x = zip(HP, MPG, color_list, WEIGHT)
x = filter(lambda item: item[0] != 0, x)
x = filter(lambda item: item[1] != 0, x)
x = filter(lambda item: item[3] != 0, x)

"""
for i in x:
    if 0 in i:
        x.remove(i)
"""
Hp, Mpg, colorr, weight = map(list, zip(*x))

"""
Mpg = np.array(MPG)
weight = np.array(WEIGHT)
Hp = np.array(HP)[Mpg != 0].tolist()
colorr = np.array(color_list)[Mpg != 0].tolist()
weight= np.array(WEIGHT)[Mpg != 0].tolist()
Mpg = Mpg[Mpg != 0].tolist()

"""


r_patch = mpatches.Patch(color='red', label= 'Small/Sporty/Compact/Large Sedan')
b_patch = mpatches.Patch(color='blue', label='Sports Car')
g_patch = mpatches.Patch(color='green', label='SUV')
p_patch = mpatches.Patch(color='purple', label='Wagon')
bl_patch = mpatches.Patch(color='black', label='Minivan')
c_patch = mpatches.Patch(color='cyan', label='Pickup')

tempw = []
for w in weight:
    tempw.append(w * .005)

weight = tempw


plt.scatter(Hp, Mpg, s=weight, marker="s", color=colorr)
plt.legend(handles=[r_patch,b_patch,g_patch,p_patch,bl_patch,c_patch])
plt.xlabel('Horsepower')
plt.ylabel('City MPG')
plt.title('Horsepower vs City MPG for vehicles')
plt.savefig(sys.argv[2])
