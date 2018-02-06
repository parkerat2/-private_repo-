import matplotlib.pyplot as plt
import pip
pip.main(['install','pandas'])
import pandas as pd
import seaborn
import sys

df = pd.read_csv(sys.argv[1])
df = df[["HP", "City MPG", "Weight", "Small/Sporty/ Compact/Large Sedan", "Sports Car", "SUV", "Wagon", "Minivan", "Pickup"]]
df = df[df["City MPG"] != '*']
df = df[df["Weight"] != '*']


def cat(row):
    if row['Small/Sporty/ Compact/Large Sedan'] == 1:
        return 'Small/Sporty/ Compact/Large Sedan'
    if row['Sports Car'] == 1:
        return 'Sports Car'
    if row['SUV'] == 1:
        return 'SUV'
    if row['Wagon'] == 1:
        return 'Wagon'
    if row['Minivan'] == 1:
        return 'Minivan'
    if row['Pickup'] == 1:
        return 'Pickup'
    else:
        return 'no cat'


categories = []
for index, row in df.iterrows():
    categories.append(cat(row))

df['category'] = categories
columns = ["Small/Sporty/ Compact/Large Sedan", "Sports Car", "SUV", "Wagon", "Minivan", "Pickup"]
df.drop(columns, inplace=True, axis=1)
# print(df)
# pd.set_option('display.max_rows', 500)
df["City MPG"] = pd.to_numeric(df["City MPG"])
df["Weight"] = pd.to_numeric(df["Weight"])

colors = {'Small/Sporty/ Compact/Large Sedan': 'red', 'Sports Car': 'green', 'SUV': 'blue',
          'Wagon': 'magenta', 'Minivan': 'cyan', 'Pickup': 'yellow'}
plot = df.plot(x="HP", y="City MPG", s=df['Weight'] / 10, c=df['category'].apply(lambda x: colors[x]),
               kind='scatter', figsize = (7,7), title='Cars')
plot.set_xlabel("HP")
plot.set_ylabel("City MPG")

plt.savefig(sys.argv[2])
