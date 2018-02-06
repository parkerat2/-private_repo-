import csv
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib.patches import Polygon
import matplotlib.patches as patches
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import sys


def read_file():
   table_list = []
   with open( sys.argv[1]) as csvfile:
           readCSV = csv.reader(csvfile, delimiter=',')
           for row in readCSV:
               if len(row) > 0:
                   table_list.append(row)
   return table_list


def main():
   final = []
   table = read_file()
   table_clean = table[1:]
   table_clean = [i[0:4] for i in table_clean]
   for row in table_clean:
       final.append([float(i) for i in row])

   x = StandardScaler().fit_transform(final)
   pca = PCA(n_components=4)
   X_r = pca.fit_transform(x)


   for i in range(0, len(X_r)):
       X = X_r[i][0] * -1
       Y = X_r[i][2] * -1
       four = final[i][0]
       tree = final[i][1] 
       two = final[i][2] 
       one = final[i][3] 
       Path = mpath.Path
       path_data = [
       (Path.MOVETO, (-two, 0)),
       (Path.LINETO, (0, four)),
       (Path.LINETO, (tree, 0)),
       (Path.LINETO, (0, -one)),
       (Path.LINETO, (-two, 0)),
       (Path.LINETO, (tree, 0)),
       (Path.MOVETO, (0, -one)),
       (Path.LINETO, (0, four)),
       ]
       codes, verts = zip(*path_data)
       markerp = mpath.Path(verts, codes)
       plt.scatter(X, Y, marker=markerp, s=300, facecolors='none', edgecolors='g')

       plt.xlabel("PCA1")
       plt.ylabel("PCA2")
       plt.title("iris DataSet PCA")







   plt.savefig(sys.argv[2])






if __name__ == '__main__':
   main()

