#Dillon Carns
#2/4/2018
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import random as r
import sys

df = pd.read_csv(sys.argv[1],skiprows=[0], names=['sepal length','sepal width','petal length','petal width','class'])

#print(df['petal length'])

#standardize the data set
from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width']

#separate out features
x = df.loc[:,['sepal width', 'petal width']].values

# Separating out the target
y = df.loc[:,['class']].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['PC1', 'PC2'])

finalDf = pd.concat([principalDf, df[['class']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
#ax.set_xlabel('Principal Component 1', fontsize = 15)
#ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 Component PCA with Iris Dataset', fontsize = 20)

classes = ['Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
colors = 'g', 'g', 'g'
df.drop('class', axis=1, inplace=True)
for target, color in zip(classes,colors):
	indicesToKeep = finalDf['class'] == target
	verts = [[r.randint(1, 2), 0], [0,1], [-1, 0], [0, -1], [1, 0], [-1, 0], [0, -1], [0, 1]]
	#print(verts)
	plt.scatter(finalDf.loc[indicesToKeep,'PC1']
		,finalDf.loc[indicesToKeep, 'PC2']
	 	,c = None, edgecolor=color, facecolor='w'
         	,s = 100, verts=verts)
#plt.show()
plt.savefig(sys.argv[2])









