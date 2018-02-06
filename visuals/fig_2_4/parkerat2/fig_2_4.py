import pandas as pd
import sys
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

args = sys.argv
df = pd.read_csv(args[1])
# df = pd.read_csv("iris.csv")
headers = list(df)
X = df.as_matrix(columns=headers[0:-1])

pca = PCA(n_components=2)
Xpca = pca.fit_transform(X)

x = [i[0] for i in Xpca]
y = [i[1] for i in Xpca]

Xn = X / X.max(0)
patches = []
for i in range(len(x)):
    poly = Polygon([[x[i] + Xn[i][2] / 10, y[i]], [x[i], y[i] + Xn[i][1] / 10], [x[i] - Xn[i][0] / 10, y[i]], [x[i], y[i] - Xn[i][3] / 10]])
    horz = Polygon([[x[i] + Xn[i][2] / 10, y[i]], [x[i] - Xn[i][0] / 10, y[i]]])
    vert = Polygon([[x[i], y[i] + Xn[i][1] / 10], [x[i], y[i] - Xn[i][3] / 10]])
    patches.append(poly)
    patches.append(horz)
    patches.append(vert)
    plt.scatter(x[i], y[i], s=1/2, marker='+', color='g')
p = PatchCollection(patches)
p.set_color('g')
p.set_facecolor('none')
ax = plt.gca()
ax.add_collection(p)
ax.invert_xaxis()
# ax.invert_yaxis()
plt.xticks([])
plt.yticks([])
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('Iris Dataset')

# plt.show()
plt.savefig(args[2])
plt.clf()
