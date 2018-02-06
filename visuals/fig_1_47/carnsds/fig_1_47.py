#Dillon Carns
#1/28/2018
import matplotlib.pyplot as plt
import pandas as pand

import sys

fields = ['Small/Sporty/ Compact/Large Sedan','Sports Car','SUV','Wagon', 'Minivan',
'Pickup','HP', 'City MPG', 'Weight']
df = pand.read_csv(sys.argv[1], skipinitialspace=True, usecols=fields)


plt.title("City MPG vs Horse Power for a Lot of Cars")
plt.xlabel("HP")
plt.ylabel("City MPG")
plt.scatter(df.loc[df['Small/Sporty/ Compact/Large Sedan'] == 1, 'HP'],
 df.loc[df['Small/Sporty/ Compact/Large Sedan'] == 1, 'City MPG'], c='k', marker='s')
plt.scatter(df.loc[df['Sports Car'] == 1, 'HP'],
 df.loc[df['Sports Car'] == 1, 'City MPG'], c='g', marker='s')
plt.scatter(df.loc[df['SUV'] == 1, 'HP'],
 df.loc[df['SUV'] == 1, 'City MPG'], c='b', marker = 's')
plt.scatter(df.loc[df['Wagon'] == 1, 'HP'],
 df.loc[df['Wagon'] == 1, 'City MPG'], c='r', marker = 's')
plt.scatter(df.loc[df['Minivan'] == 1, 'HP'],
 df.loc[df['Minivan'] == 1, 'City MPG'], c='m', marker = 's')
plt.scatter(df.loc[df['Pickup'] == 1, 'HP'],
 df.loc[df['Pickup'] == 1, 'City MPG'], c='y', marker = 's')
plt.legend(['Compact', 'Sports Cars', 'SUV', 'Wagon', 'Minivan', 'Pickup'])
plt.savefig(sys.argv[2], Transparent=True)

