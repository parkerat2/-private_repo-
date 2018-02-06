#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import PCA

data = pd.read_csv(sys.argv[1], usecols=["sepal length", "sepal width", "petal length", "petal width"])
results = np.array(data)
pca = PCA(results)
pca.Y[:,0] = pca.Y[:,0] * -1
pca.Y[:,1] = pca.Y[:,1] * -1
plt.scatter(pca.Y[:,0], pca.Y[:,1], s=1)
i = 0
while i < len(pca.Y[:,0]):
	x1 =[pca.Y[i,0] - (results[i,0]/50), pca.Y[i,0] + (results[i,1]/50)]
	y1 =[pca.Y[i,1] - (results[i,2]/10), pca.Y[i,1] + (results[i,3]/10)]
	plt.hlines(y=pca.Y[i,1], xmin=x1[0], xmax=x1[1], color='green')
	plt.vlines(x=pca.Y[i,0], ymin=y1[0], ymax=y1[1], color='green')
	plt.plot([x1[0], pca.Y[i,0]], [pca.Y[i,1], y1[0]], color='green', linewidth=.7)
	plt.plot([x1[0], pca.Y[i,0]], [pca.Y[i,1], y1[1]], color='green', linewidth=.7)
	plt.plot([x1[1], pca.Y[i,0]], [pca.Y[i,1], y1[0]], color='green', linewidth=.7)
	plt.plot([x1[1], pca.Y[i,0]], [pca.Y[i,1], y1[1]], color='green', linewidth=.7)
	#plt.plot(x1[0], pca.Y[i,1], pca.Y[i,0], y1[0])
	i+=1

#fig,ax = plt.subplots(1)

#ax.set_yticklabels([])
#ax.set_xticklabels([])
plt.xlabel("left = sepal length, Right = sepal width (divided by 50)")
plt.ylabel("down = petal length, up = petal width (divied by 10)")
plt.xticks([])
plt.yticks([])

plt.savefig(sys.argv[2])
