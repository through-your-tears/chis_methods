from math import *
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from numbers import Number


class Vector(list):
    def __init__(self, other=None):
        if other is None:
            super().__init__()
        else:
            super().__init__(other)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if len(other) != len(self):
                raise IndexError
            else:
                for i in range(len(self)):
                    self[i] += other[i]
                return self
        else:
            raise TypeError

    def __isub__(self, other):
        if isinstance(other, Vector):
            if len(other) != len(self):
                raise IndexError
            else:
                for i in range(len(self)):
                    self[i] -= other[i]
                return self
        else:
            raise TypeError

    def __imul__(self, other):
        if isinstance(other, Number):
            for i in range(len(self)):
                self[i] *= other
            return self
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(other) != len(self):
                raise IndexError
            else:
                ans = deepcopy(self)
                for i in range(len(self)):
                    ans[i] += other[i]
                return ans
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(other) != len(self):
                raise IndexError
            else:
                ans = deepcopy(self)
                for i in range(len(self)):
                    ans[i] -= other[i]
                return ans
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Number):
            ans = deepcopy(self)
            for i in range(len(ans)):
                ans[i] *= other
            return ans
        else:
            raise TypeError


def count_vector(functions, x, y) -> Vector:
    return Vector([func(x, y) for func in functions])


def rounge_kout_formula(functions, x, y, h):
    k1 = count_vector(functions, x, y)
    k2 = count_vector(functions, x - h / 2, y - k1 * (h / 2))
    k3 = count_vector(functions, x - h / 2, y - k2 * (h / 2))
    k4 = count_vector(functions, x - h, y - k3 * h)
    return (k1 + k2 * 2 + k3 * 2 + k4) * (h / 6) + y


def rounge_kout(func, a, b, h, x, y):
    coords = Vector()
    n = (a - b) / h
    i = 0
    while i < round(n):
        y = rounge_kout_formula(func, x, y, h)
        coords.append(Vector((x, y)))
        x -= h
        i += 1
    return coords


def adams_formula(functions, points, h, y):
    return (count_vector(functions, *points[4]) * 1901 - count_vector(functions, *points[3]) * 2774 +
            count_vector(functions, *points[2]) * 2616 - count_vector(functions, *points[1]) * 1274 +
            count_vector(functions, *points[0]) * 251) * (h / 720) + y


def adams(functions, koshi_data, eps):
    coords = rounge_kout(functions, koshi_data[0], koshi_data[0] - eps * 5, eps, koshi_data[0], koshi_data[1])
    coords.reverse()
    graph_coords = Vector([(koshi_data[0], koshi_data[1],)])
    j = koshi_data[0] + eps
    while j <= koshi_data[-1]:
        a = adams_formula(functions, coords, eps, graph_coords[-1][-1])
        graph_coords.append((j, a))
        coords.append((j, a))
        coords.pop(0)
        j += eps
    return graph_coords


def find_nevyazka(graph_coords, anal_function):
    mn = 0
    for x in graph_coords:
        for j in range(len(x)):
            if abs(anal_function[j](x[0]) - x[1][j]) > mn:
                mn = abs(anal_function[j](x[0]) - x[1][j])
    return mn


def main():
    functions = [
        (
            lambda t, y: y[0] - y[1] + 2 * sin(t),
            lambda t, y: 2 * y[0] - y[1],
        ),
        (
            lambda t, y: t / y[1],
            lambda t, y: -1 * t / y[0]
        ),
        (
            lambda t, y: 2 * y[0] - y[1] - y[2],
            lambda t, y: 3 * y[0] - 2 * y[1] - 3 * y[2],
            lambda t, y: -1 * y[0] + y[1] + 2 * y[2]
        )
    ]
    anal_functions = [
        (
            lambda x: cos(x) + sin(x) + x * sin(x) - x * cos(x),
            lambda x: 3 * sin(x) - 2 * x * cos(x) + cos(x)
        ),
        (
            lambda x: exp(x ** 2),
            lambda x: 1 / (2 * exp(x ** 2))
        ),
        (
            lambda x: 3 * exp(x),
            lambda x: exp(x),
            lambda x: 2 * exp(x)
        )
    ]
    koshi_data = [
        (-10, Vector([-14.126, -15.9884]), 10.01),
        (-1.5, Vector([9.48774, 0.0527]), 1.51),
        (0, Vector([3, 1, 2]), 5.11)
    ]
    epsilons = (
        0.2,
        0.064,
        0.3
    )
    for i in range(len(koshi_data)):
        eps = epsilons[i]
        graph_coords = adams(functions[i], koshi_data[i], eps)
        eps /= 2
        graph_coords_any = adams(functions[i], koshi_data[i], eps)
        for j in range(len(functions[i])):
            plt.plot(np.array([deepcopy(a[0]) for a in graph_coords]),
                     np.array([deepcopy(a[1][j]) for a in graph_coords]), label=f'функция {j}, h = {eps * 2}')
        for j in range(len(functions[i])):
            plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                     np.array([deepcopy(a[1][j]) for a in graph_coords_any]), label=f'функция {j}, h = {eps}')
        for j in range(len(functions[i])):
            plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                     np.array([anal_functions[i][j](deepcopy(a[0])) for a in graph_coords_any]),
                     label=f' функция {j} Точное')
        plt.legend()
        plt.show()
        n1 = find_nevyazka(graph_coords, anal_functions[i])
        mn = find_nevyazka(graph_coords_any, anal_functions[i])
        print(f'''Максимальная погрешность на 1 решении = {n1
        }, Максимальная погрешность на 2 решении = {mn}, Отношение погрешностей = {n1 / mn}''')


if __name__ == '__main__':
    main()
