import sys

from pandas import read_csv
from ggplot import *

#df = read_csv('http://cs.appstate.edu/~rmp/cs5720/cars04.csv')
df = read_csv(sys.argv[1])

df = df.drop(df[(df['City MPG'] == '*')].index)
df = df.drop(df[(df['Weight'] == '*')].index)

def get_type():
    tmp = df['Vehicle Name'].values
    for i in range(len(tmp)):
        if(df['Small/Sporty/ Compact/Large Sedan'].values[i] == 1):
            tmp[i] = 'Sedan'
        elif df['SUV'].values[i] == 1:
            tmp[i] = 'SUV'
        elif df['Sports Car'].values[i] == 1:
            tmp[i] = 'Sport Car'
        elif df['Wagon'].values[i] == 1:
            tmp[i] = 'Wagon'
        elif df['Pickup'].values[i] == 1:
            tmp[i] = 'Pickup'
        else:
            tmp[i] = 'Minivan'
    return tmp

df['Type'] = get_type()
df['City MPG'] = df['City MPG'].astype(int)
df['Weight'] = df['Weight'].astype(int)/100

    #geom_point(aes(size = 'Weight')) +\
p=ggplot(df, aes(x='City MPG', y='HP', color = 'Type')) +\
    geom_point() +\
    xlab("City MPG") + ylab("HP") + ggtitle("City MPG v Horsepower")

p.save(sys.argv[2])
