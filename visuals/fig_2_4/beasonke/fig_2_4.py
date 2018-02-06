import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
# import bokeh.plotting, bokeh.models
# bokeh.plotting.output_notebook()
import sys

df= pd.read_csv(sys.argv[1])
# df = df[["sepal length", "sepal width", "petal length", "petal width"]]
x = df.ix[:,0:4].values
y = df.ix[:,4].values
X_std = StandardScaler().fit_transform(x)
c = np.cov(X_std.T)
eig_vals, eig_vecs = np.linalg.eig(c)

#create and sort eigenvalue, eigenvector pairs
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
eig_pairs.sort(key=lambda x: x[0], reverse=True)
eig_mat = np.column_stack((eig_pairs[0][1], eig_pairs[1][1]))
# print(eig_mat)
Y = X_std.dot(eig_mat)

with plt.style.context('seaborn-whitegrid'):
    x = Y[:,0]
    y = Y[:,1]
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, marker='.')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(loc='lower center')
    plt.tight_layout()
    plt.plot()
    #plt.show()
plt.savefig(sys.argv[2])

