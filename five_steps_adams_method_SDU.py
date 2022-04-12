from math import *
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np


def rounge_kout_formula(func, x, y, h, prev):
    k1 = func(x, y)
    k2 = func(x - h / 2, y - h * k1 / 2)
    k3 = func(x - h / 2, y - h * k2 / 2)
    k4 = func(x - h, y - h * k3)
    return h / 6 * (k1 + 2 * k2 + 2 * k3 + k4) + prev


def rounge_kout(func, a, b, h, x, y):
    coords = []
    n = (a - b) / h
    i = 0
    while i < round(n):
        y = rounge_kout_formula(func, x, y, h, y)
        coords.append((x, y))
        x -= h
        i += 1
    return coords


def adams(func, points, h, y):
    return h/720 * (1901 * func(*points[4]) - 2774 * func(*points[3]) +
                    2616 * func(*points[2]) - 1274 * func(*points[1]) + 251 * func(*points[0])) + y


def main():
    functions = np.array([
        (
            lambda x, y, t: x - y + 2 * sin(t),
            lambda x, y: 2 * x - y
        ),
        (
            lambda x, y, z: x / z,
            lambda x, y, z: -1 * x / y
        ),
    ])
    anal_functons = np.array([
        (
            lambda x: cos(x) + sin(x) + x * sin(x) - x * cos(x),
            lambda x: 3 * sin(x) - 2 * x * cos(x) + cos(x)
        ),
        (
            lambda x: exp(x ** 2),
            lambda x: 1 / 2 * exp(x ** 2)
        )
    ])
    koshi_data = [
        (-10, -14.126, 10),
        (-1.5, 9.48774, 1.5)
    ]
    for i in range(len(koshi_data)):
        eps = 0.08
        coords = rounge_kout(functions[i], koshi_data[i][0], koshi_data[i][0] - eps * 5, eps, koshi_data[i][0],
                       koshi_data[i][1])
        coords.reverse()
        graph_coords = [(koshi_data[i][0], koshi_data[i][1],)]
        j = koshi_data[i][0] + eps
        while j <= koshi_data[i][-1]:
            a = adams(functions[i], coords, eps, graph_coords[-1][-1])
            graph_coords.append((j, a))
            coords.append((j, a))
            coords.pop(0)
            j += eps
        eps /= 2
        coords = rounge_kout(functions[i], koshi_data[i][0], koshi_data[i][0] - eps * 5, eps, koshi_data[i][0],
                       koshi_data[i][1])
        coords.reverse()
        graph_coords_any = [(koshi_data[i][0], koshi_data[i][1],)]
        j = koshi_data[i][0] + eps
        while j <= koshi_data[i][-1]:
            a = adams(functions[i], coords, eps, graph_coords_any[-1][-1])
            graph_coords_any.append((j, a))
            coords.append((j, a))
            coords.pop(0)
            j += eps
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords]),
                 np.array([deepcopy(a[1]) for a in graph_coords]), label=f'h = {eps * 2}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any],),
                 np.array([deepcopy(a[1]) for a in graph_coords_any]),  label=f'h = {eps}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([anal_functons[i](deepcopy(a[0])) for a in graph_coords_any]), label='Точное')
        plt.legend()
        plt.show()
        mn = 0
        for x in graph_coords:
            if abs(anal_functons[i](x[0]) - x[1]) > mn:
                mn = abs(anal_functons[i](x[0]) - x[1])
        n1 = mn
        mn = 0
        for x in graph_coords_any:
            if abs(anal_functons[i](x[0]) - x[1]) > mn:
                mn = abs(anal_functons[i](x[0]) - x[1])
        print(f'''Максимальная невязка на 1 решении = {n1
        }, Максимальная невязка на 2 решении = {mn}, Отношение невязок = {n1 / mn}''')


if __name__ == '__main__':
    main()