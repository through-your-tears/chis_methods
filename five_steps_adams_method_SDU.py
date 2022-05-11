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


def adams(functions, points, h, y):
    return (count_vector(functions, *points[4]) * 1901 - count_vector(functions, *points[3]) * 2774 +
            count_vector(functions, *points[2]) * 2616 - count_vector(functions, *points[1]) * 1274 +
            count_vector(functions, *points[0]) * 251) * (h / 720) + y
    # return (func(*points[4]) * 1901 - func(*points[3]) * 2774 +
    #         func(*points[2]) * 2616 - func(*points[1]) * 1274 + func(*points[0]) * 251) * (h / 720) + y


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
    ]
    anal_functons = [
        (
            lambda x: cos(x) + sin(x) + x * sin(x) - x * cos(x),
            lambda x: 3 * sin(x) - 2 * x * cos(x) + cos(x)
        ),
        (
            lambda x: exp(x ** 2),
            lambda x: 1 / (2 * exp(x ** 2))
        )
    ]
    koshi_data = [
        (-10, Vector([-14.126, -15.9884]), 10.01),
        (-1.5, Vector([9.48774, 0.0527]), 1.51),
    ]
    epsilons = (
        0.2,
        0.064
    )
    for i in range(len(koshi_data)):
        eps = epsilons[i]
        coords = rounge_kout(functions[i], koshi_data[i][0], koshi_data[i][0] - eps * 5, eps, koshi_data[i][0],
                             koshi_data[i][1])
        coords.reverse()
        graph_coords = Vector([(koshi_data[i][0], koshi_data[i][1],)])
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
                 np.array([deepcopy(a[1][0]) for a in graph_coords]), label=f'h = {eps * 2}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords]),
                 np.array([deepcopy(a[1][1]) for a in graph_coords]), label=f'h = {eps * 2}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([deepcopy(a[1]) for a in graph_coords_any]), label=f'h = {eps}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([anal_functons[i][0](deepcopy(a[0])) for a in graph_coords_any]), label='Точное')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([anal_functons[i][1](deepcopy(a[0])) for a in graph_coords_any]), label='Точное')
        plt.legend()
        plt.show()
        mn = 0
        for x in graph_coords:
            for j in range(len(x)):
                if abs(anal_functons[i][j](x[0]) - x[1][j]) > mn:
                    mn = abs(anal_functons[i][j](x[0]) - x[1][j])
        n1 = mn
        mn = 0
        for x in graph_coords_any:
            for j in range(len(x)):
                if abs(anal_functons[i][j](x[0]) - x[1][j]) > mn:
                    mn = abs(anal_functons[i][j](x[0]) - x[1][j])
        print(f'''Максимальная невязка на 1 решении = {n1
        }, Максимальная невязка на 2 решении = {mn}, Отношение невязок = {n1 / mn}''')


if __name__ == '__main__':
    main()
