import matplotlib.pyplot as plt
import sys
import pandas as pd
import numpy as np

# city MPG vs Horsepower
# color for vehicle type
# size for weight (area proportional to weight


def main():
    #car_data = pd.read_csv('cars04.csv')
    car_data = pd.read_csv(sys.argv[1])
    car_data = car_data.reset_index()
    car_data = car_data[['Small/Sporty/ Compact/Large Sedan','Sports Car','SUV','Wagon', 'Minivan','Pickup','HP','City MPG','Weight']]
    car_data = car_data.rename(columns=lambda x:x.strip().replace(' ','_'))
    car_data = car_data.rename(columns=lambda x:x.strip().replace('/','_'))
    car_data = car_data.replace('*', np.nan)
    car_data = car_data.dropna(subset=['HP'])
    car_data = car_data.dropna(subset=['City_MPG'])
    car_data = car_data.dropna(subset=['Weight'])
    car_data = car_data.reset_index()

    small = car_data.drop(car_data[car_data.Small_Sporty__Compact_Large_Sedan < 1].index)
    small = small.reset_index()
    sport = car_data.drop(car_data[car_data.Sports_Car < 1].index)
    sport = sport.reset_index()
    suv = car_data.drop(car_data[car_data.SUV < 1].index)
    suv = suv.reset_index()
    wagon = car_data.drop(car_data[car_data.Wagon < 1].index)
    wagon = wagon.reset_index()
    minivan = car_data.drop(car_data[car_data.Minivan < 1].index)
    minivan = minivan.reset_index()
    pick = car_data.drop(car_data[car_data.Pickup < 1].index)
    pick = pick.reset_index()
    fig, ax = plt.subplots()
    ax.scatter(small['HP'], small['City_MPG'], s=[2**(float(n)/1000) for n in small['Weight']], c='blue', marker='s', label='Small/Sporty/Compact/Large Sedan')
    ax.scatter(sport['HP'], sport['City_MPG'], s=[2**(float(n)/1000) for n in sport['Weight']], c='red', marker='s', label='Sports Car')
    ax.scatter(suv['HP'], suv['City_MPG'], s=[2**(float(n)/1000) for n in suv['Weight']], c='black', marker='s', label='SUV')
    ax.scatter(wagon['HP'], wagon['City_MPG'], s=[2**(float(n)/1000) for n in wagon['Weight']], c='brown', marker='s', label='Wagon')
    ax.scatter(minivan['HP'], minivan['City_MPG'], s=[2**(float(n)/1000) for n in minivan['Weight']], c='yellow', marker='s', label='Minivan')
    ax.scatter(pick['HP'], pick['City_MPG'], s=[2**(float(n)/1000) for n in pick['Weight']], c='green', marker='s', label='Pickup')

    ax.set_xlabel('HP')
    ax.set_ylabel('City MPG')
    ax.set_title('City MPG vs. Horsepower')
    ax.legend(loc='upper right', shadow=True, markerscale=1)

    #plt.show()
    print(sys.argv[2])
    plt.savefig(sys.argv[2])


if __name__ == '__main__':
    main()
