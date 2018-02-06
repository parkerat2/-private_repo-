import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import sys


file = sys.argv[1]
data = pd.read_csv(file, header=None, sep=',')
#get the data of just the values not the species names
X = data.ix[:,0:3].values

#get the species names
y = data.ix[:,4:].values

#remove the first element which is a list of the header names
columns = X[0]
X = X[1:]

#create a standardized
X_std = StandardScaler().fit_transform(X)

x0 = []
x1 = []
x2 = []
x3 = []

for e in X:
    x0.append(float(e[0]))
    x1.append(float(e[1]))
    x2.append(float(e[2]))
    x3.append(float(e[3]))

cov_mat=np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
                      eig_pairs[2][1].reshape(4,1)))


Y = X_std.dot(matrix_w)

xs = []
ys = []
for i in Y:
    xs.append(i[0])
    ys.append(i[1])


# verticies = []
# for i in range(len(xs)):
#     vert = [
#         (xs[i], ys[i]),
#         (x0[i], 0),
#         (xs[i], ys[i]),
#         (0, x1[i]),
#         (xs[i], ys[i]),
#         (x2[i],0),
#         (xs[i], ys[i]),
#         (0,-x3[i]),
#     ]
#     verticies.append(vert)
#
# Path = mpath.Path
# codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
# path = mpath.Path(verticies[0], codes)
# patch = mpatches.PathPatch(path, facecolor='g')
# fig, ax = plt.subplots()
# ax.add_patch(patch)

plt.scatter(xs, ys, color='green',marker='+')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('Pricipal component analysis of the Iris dataset')
plt.savefig(sys.argv[2])
