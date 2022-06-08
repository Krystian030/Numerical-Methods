import copy
import csv
import sys
import time
from lagrange import *
from spline import *
import matplotlib.pyplot as plt

result_path = './Result/'


def read_data_csv(file_name):
    path = './Data/' + file_name + '.csv'
    with open(path) as csv_file:
        reader = csv.reader(csv_file)
        # data (x, h)
        data = []
        try:
            header = next(reader)  # check file content's header
            check_header = False
            for i, row in enumerate(reader):
                if type(header[0]) is float and not check_header:
                    data.append((i, float(header[1])))
                    check_header = True
                data.append((i, float(row[1])))
            return data
        except csv.Error as error:
            sys.exit(error)


def get_x(data):
    return [x[0] for x in data]


def get_height(data):
    return [height[1] for height in data]


def draw_chart(interpolation_data, input_nodes, data, file_name, place):
    data = data[0:input_nodes[-1][0]+1]
    x, height = get_x(data), get_height(data)
    x_interpolation, height_interpolation = get_x(interpolation_data), get_height(interpolation_data)
    x_calc, y_calc = get_x(input_nodes), get_height(input_nodes)

    plt.plot(x, height, '.', markersize=1, label='funkcja interpolowana')
    plt.plot(x_interpolation, height_interpolation, label='funkcja interpolująca')
    plt.plot(x_calc, y_calc, 'o', markersize=3, label='węzły interpolowane')
    plt.yscale('log')
    # plt.ylim(ymin=min(height)-1)
    plt.xlabel('Punkt')
    plt.ylabel('Wysokość [m]')
    plt.legend()

    plt.title(f'{file_name} - {str(len(input_nodes))} węzłów')
    chart = f'{result_path}\\{file_name}\\interpolation_{place}_{file_name}_{str(len(input_nodes))}.png'
    plt.savefig(chart)
    plt.close()


def draw_rout(data, rout_name):
    x, height = get_x(data), get_height(data)

    plt.plot(x, height, label=f'Trasa: {rout_name}')
    plt.ylim(ymin=0)
    plt.xlabel('Punkt')
    plt.ylabel('Wysokość [m]')
    plt.legend()

    plt.title(f'{rout_name}')
    chart = f'{result_path}\\{rout_name}.png'
    plt.savefig(chart)
    plt.close()


# SpacerniakGdansk, WielkiKanionKolorado, MountEverest
# files_name = ['WielkiKanionKolorado', 'Obiadek', 'MountEverest', '100', 'GlebiaChallengera', 'Hel_yeah', 'Redlujjj', 'SpacerniakGdansk']
files_name = ['rozne_wniesienia', 'chelm', 'MountEverest', 'WielkiKanionKolorado', 'SpacerniakGdansk']

for file in files_name:
    data = read_data_csv(file)
    # steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    steps = [5, 10, 15, 50, 100, 200]
    draw_rout(data, file)
    for step in steps:
        interpolation_data, input_nodes = spline_interpolation(step, data)
        draw_chart(interpolation_data, input_nodes, data, 'Spline', file)

    for step in steps:
        interpolation_data, input_nodes = lagrange_interpolation(step, data)
        draw_chart(interpolation_data, input_nodes, data, 'Lagrange', file)
