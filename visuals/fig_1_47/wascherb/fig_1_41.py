import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import numpy as np
import sys


def results(file_name):
    """
    clean data for representation
    :param file_name: input filename for data
    :return: None
    """

    x = []
    y = []
    car_type = []
    size = []
    leg_names = []
    cnt = 0
    index_x, index_y = 0, 0
    with open(file_name) as f:
        for line in f:
            content = str(line).strip()
            elements = content.split(',')

            if cnt != 0:
                last_element = len(elements) - 1
                try:
                    if elements[index_x].isdigit() and elements[index_y].isdigit():
                        x.append(int(elements[index_x]))
                        y.append(int(elements[index_y]))
                        if str(elements[last_element])[:-1].isdigit() and elements[last_element - 1].isdigit() and \
                                elements[last_element - 3].isdigit():
                            car_type.append(elements.index('1'))
                            area = int(str(elements[last_element])[:-1]) * int(elements[last_element - 1])
                            weight = int(elements[last_element - 3])
                            size.append(area / weight * 250)
                        else:
                            car_type.append(7)
                            # print('%-30s: %s' % (elements[0], elements.index('1')))
                            # size.append(0.3567027132923991 * 250)
                            # print('FAULT')
                except:
                    print(elements[index_x])
                    print(elements[index_y])
            else:
                index_x = elements.index('HP')
                index_y = elements.index('City MPG')
                for i in range(1, 7):
                    leg_names.append(elements[i])
                leg_names.append('No data for size')
            cnt += 1

    plot(x, y, car_type, size, leg_names)


def plot(x, y, car_type, size, leg_names):
    """
    creating the scatter plot of the data
    :param x: HP data
    :param y: MPG data
    :param car_type: type classes
    :param size: sizes of rectangles
    :param leg_names: legend names extracted from the data sorces
    :return: None
    """

    plt.title('City MPG / HP for each type of car in relation to the car size')

    color_map = {1: 'green', 2: 'orange', 3: 'teal', 4: 'maroon', 5: 'yellow', 6: 'red', 7: 'silver'}
    colors = []
    for index, type in enumerate(car_type):
        colors.append(color_map[type])
        car_type[index] = color_map[type]

    plt.scatter(x, y, color=colors, s=size, marker='s', edgecolors='black')
    plt.xlabel('HP')
    plt.ylabel('City MPG')

    # scale steps
    plt.yticks(np.arange(10, 65, 5))
    plt.xticks(np.arange(min(x), max(x) + 42.7, 42.7))

    # Add legend
    recs = []
    for i in color_map.values():
        recs.append(mpatches.Rectangle((0, 0), 1, 1, fc=i))
    plt.legend(recs, leg_names, loc=1)

    # plt.show()
    plt.savefig(sys.argv[2])


if __name__ == '__main__':
    if sys.argv == 1:
        print('Accept one argument: No input file for data')
        exit(0)

    results(sys.argv[1])
