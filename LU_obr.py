from fractions import Fraction
from copy import deepcopy
from obr_matrix import obr_matrix


def mul_matrix(a, b):
    n = len(a)
    m = len(b[0])
    p = len(a[0])
    result_matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result_matrix[i][j] += a[i][k] * b[k][j]
    return result_matrix


def LU_obr(a):
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
    uo = obr_matrix(u)
    lo = obr_matrix(l)
    return mul_matrix(uo, lo)


if __name__ == '__main__':
    p = int(input())
    matrix = [[Fraction(a) for a in input().split()] for i in range(p)]
    res = LU_obr(matrix)
    for row in res:
        print(*row)
