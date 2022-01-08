import matplotlib.pyplot as plt
import numpy as np
from gauss import gauss
from fractions import Fraction
from copy import deepcopy
from math import *


def least_squares_method(m, points):
    n = len(points)
    b = [[Fraction() for j in range(m)] for i in range(m)]
    for k in range(m):
        for l in range(m):
            for i in range(n):
                b[k][l] += points[i][0] ** (k + l)
        c = Fraction()
        for i in range(n):
            c += points[i][0] ** k * points[i][1]
        b[k].append(c)
    return gauss(b)


def local_smoothing_of_data(n, m, k, points):
    for i in range(n):
        if k // 2 < i < n - k // 2:
            op = points[i - k // 2: i + k // 2 + 1]
        elif k // 2 > i:
            op = points[:i + k // 2 + 1]
        else:
            op = points[i - k // 2:]
        y = least_squares_method(m, op)
        s = 0
        for j in range(len(y)):
            s += points[i][0] ** j * y[j]
        points[i][1] = s
    return points


def main():
    m, k, a, b = [int(a) for a in input().split()]
    n = b - a + 1
    points = []
    func = input()
    i = a
    while i < b + 1:
        x = Fraction(i)
        points.append([x, Fraction(eval(func))])
        i += 0.1
    plt.plot(np.array([deepcopy(a[0]) for a in points]), np.array([deepcopy(a[1]) for a in points]))
    plt.show()
    result = local_smoothing_of_data(n, m, k, points)
    plt.plot(np.array([deepcopy(a[0]) for a in result]), np.array([deepcopy(a[1]) for a in result]))
    plt.show()


if __name__ == '__main__':
    main()