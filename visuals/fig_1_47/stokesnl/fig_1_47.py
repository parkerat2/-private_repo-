#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import sys

columns = defaultdict(list) # each value in each column is appended to a list

with open(sys.argv[1]) as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
#test = ['225', '125', '231']
toremove = []
for i in range(1,len(columns['HP'])):
    if columns['City MPG'][i] == '*':
        toremove.append(i)
for i in reversed(toremove):
    del columns['HP'][i]
    del columns['City MPG'][i]
    del columns['Weight'][i]
    del columns['Small/Sporty/ Compact/Large Sedan'][i]
    del columns['Sports Car'][i]
    del columns['SUV'][i]
    del columns['Wagon'][i]
    del columns['Minivan'][i]
    del columns['Pickup'][i]
toremove = []
for i in range(1,len(columns['Weight'])):
    if columns['Weight'][i] == '*':
        toremove.append(i)
for i in reversed(toremove):
    del columns['HP'][i]
    del columns['City MPG'][i]
    del columns['Weight'][i]
    del columns['Small/Sporty/ Compact/Large Sedan'][i]
    del columns['Sports Car'][i]
    del columns['SUV'][i]
    del columns['Wagon'][i]
    del columns['Minivan'][i]
    del columns['Pickup'][i]
sedan = []
sports =[]
suv = []
wagon = []
minivan = []
pickup = []
for i in range(1,len(columns['Weight'])):
    if columns['Small/Sporty/ Compact/Large Sedan'][i] == '1':
        sedan.append(i)
    elif columns['Sports Car'][i] == '1':
        sports.append(i)
    elif columns['SUV'][i] == '1':
        suv.append(i)
    elif columns['Wagon'][i] == '1':
        wagon.append(i)
    elif columns['Minivan'][i] == '1':
        minivan.append(i)
    elif columns['Pickup'][i] == '1':
        pickup.append(i)
x = [float(i) for i in columns['HP']]
y = [float(i) for i in columns['City MPG']]
weight = [float(i) for i in columns['Weight']]
weight = [x / 70 for x in weight]
#[float(i) for i in columns['City MPG']]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter([columns['HP'][i] for i in sedan], [columns['City MPG'][i] for i in sedan],
s = weight, marker="s", c="yellow", edgecolors="face", label="sedans")

ax1.scatter([columns['HP'][i] for i in sports], [columns['City MPG'][i] for i in sports],
s = weight, marker="s", c="cyan",edgecolors="face", label="sports cars")

ax1.scatter([columns['HP'][i] for i in suv], [columns['City MPG'][i] for i in suv],
s = weight, marker="s", c="r",edgecolors="face", label="SUV's")

ax1.scatter([columns['HP'][i] for i in wagon], [columns['City MPG'][i] for i in wagon],
s = weight, marker="s", c="violet",edgecolors="face", label="Wagons")

ax1.scatter([columns['HP'][i] for i in minivan], [columns['City MPG'][i] for i in minivan],
s = weight, marker="s", c="b",edgecolors="face", label="Minivans")

ax1.scatter([columns['HP'][i] for i in pickup], [columns['City MPG'][i] for i in pickup],
s = weight, marker="s", c="pink",edgecolors="face", label="Pickups")
ax1.legend()
#plt.scatter(x, y, s=weight, marker="s");
plt.ylabel("City MPG")
plt.xlabel("HP")
plt.savefig(sys.argv[2]);
#print(columns['Vehicle Name'])
