import matplotlib.pyplot as plt
import numpy as np
from gauss import gauss
from fractions import Fraction
from copy import deepcopy


def least_squares_method(n, m, k, points):
    n = len(points)
    b = [[Fraction(0) for j in range(m)] for i in range(m)]
    for k in range(m):
        for l in range(m):
            for i in range(n):
                b[k][l] += points[i][0] ** (k + l)
        c = Fraction(0)
        for i in range(n):
            c += points[i][0] ** k + points[i][0]
        b[k].append(c)
    return gauss(b)


def local_smoothing_of_data(n, m, k, points):
    for i in range(n):
        if n - i > k / 2:
            op = points[i: i + k // 2 + 1]
            y = least_squares_method(n, m, k, op)
            s = 0
            for j in range(len(y)):
                s += op[j][0]**i * y[j]
            points[i][1] = y
        else:
            op = points[i:]
            y = least_squares_method(n, m, k, op)
            s = 0
            for j in range(len(y)):
                s += op[j][0] ** i * y[j]
            points[i][1] = y
    return points


def main():
    n, m, k = [int(a) for a in input().split()]
    points = [[int(a) for a in input().split()] for i in range(n)]
    plt.scatter(np.array([deepcopy(a[0]) for a in points]), np.array([deepcopy(a[1]) for a in points]))
    plt.show()
    result = local_smoothing_of_data(n, m, k, points)
    plt.scatter(np.array([deepcopy(a[0]) for a in result]), np.array([deepcopy(a[1]) for a in result]))
    plt.show()


if __name__ == '__main__':
    main()