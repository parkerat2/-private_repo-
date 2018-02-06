import csv
import numpy
import sys
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib.path as mpath


def main():
    data = []
    file_name = sys.argv[1]
    with open(file_name, 'r') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        for row in read:
            data.append(row)
    data = numpy.delete(data, 0, axis=0)
    data = numpy.delete(data, 4, axis=1)
    data = data.astype(float)
    sl_list = []
    sw_list = []
    pl_list = []
    pw_list = []
    for i in range(len(data)):
        sl_list.append(data[i][0])
        sw_list.append(data[i][1])
        pl_list.append(data[i][2])
        pw_list.append(data[i][3])
    data_s = StandardScaler().fit_transform(data)
    pca = PCA(n_components=4)
    x_r = pca.fit_transform(data_s)
    fig, ax = plt.subplots()
    for i in range(len(x_r)):
        x = x_r[i][0]
        y = x_r[i][2]
        sl = (data[i][0]-numpy.min(sl_list)+.05)/(numpy.max(sl_list)-numpy.min(sl_list)+.05)
        sl = sl*.1
        sw = (data[i][1]-numpy.min(sw_list)+.05)/(numpy.max(sw_list)-numpy.min(sw_list)+.05)
        sw = sw*.1
        pl = (data[i][2]-numpy.min(pl_list)+.05)/(numpy.max(pl_list)-numpy.min(pl_list)+.05)
        pl = pl*.1
        pw = (data[i][3]-numpy.min(pw_list)+.05)/(numpy.max(pw_list)-numpy.min(pw_list)+.05)
        pw = pw*.1
        path = mpath.Path
        path_data = [(path.MOVETO, (-x,-y)), (path.LINETO, (-x,-y+sw)), (path.MOVETO, (-x,-y)), (path.LINETO, (-x,-y-pw)),
                        (path.MOVETO, (-x,-y)), (path.LINETO, (-x+sl,-y)),(path.MOVETO, (-x,-y)), (path.LINETO, (-x-pl,-y)),
                     (path.LINETO, (-x,-y+sw)), (path.LINETO, (-x+sl,-y)),(path.LINETO, (-x,-y-pw)),(path.LINETO, (-x-pl,-y))]
        codes, verts = zip(*path_data)
        paths = mpath.Path(verts, codes)
        x1, y1 = zip(*paths.vertices)
        ax.plot(x1,y1,'g-', linewidth=.5)

    ax.set_xlabel("PCA3")
    ax.set_ylabel("PCA1")
    ax.set_title("PCA of Iris Data")
    fig.savefig(sys.argv[2])


if __name__ == '__main__':
    main()
