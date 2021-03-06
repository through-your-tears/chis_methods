from fractions import Fraction
from copy import deepcopy


def LU_det(a):
    n = len(a)
    l = [[Fraction(0) for j in range(n)] for i in range(n)]
    u = deepcopy(a)
    for i in range(n):
        for j in range(i, n):
            try:
                l[j][i] = u[j][i] / u[i][i]
            except ZeroDivisionError:
                l[j][i] = Fraction(0)
    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                try:
                    l[j][i] = u[j][i] / u[i][i]
                except ZeroDivisionError:
                    l[j][i] = Fraction(0)
        for i in range(k, n):
            for j in range(k - 1, n):
                u[i][j] = u[i][j] - l[i][k - 1] * u[k - 1][j]
    det = 1
    for i in range(n):
        det *= u[i][i]
    return det


if __name__ == '__main__':
    p = int(input())
    matrix = [[Fraction(a) for a in input().split()] for i in range(p)]
    print(LU_det(matrix))
