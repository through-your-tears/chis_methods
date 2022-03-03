from copy import deepcopy
from math import copysign

from LU_obr import mul_matrix
from obr_matrix import transpon, obr_matrix



EPS = 0.001
N = 1


def sign(x):
    return copysign(1, x)


def index_max_over_diag(matrix):
    n = len(matrix)
    m = matrix[0][1]
    k, p = 0, 1
    for i in range(1, n-1):
        for j in range(i, n):
            if matrix[i][j] > m:
                m = matrix[i][j]
                k, p = i, j
    return k, p


# def get_T(i, j, a):
#     e = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
#     t = 2 * a[i][j] / (a[i][i] - a[i][j])
#     c = ((1 + 1 / (1 + t) ** 0.5) / 2) ** 0.5
#     s = ((1 - 1 / (1 + t) ** 0.5) / 2) ** 0.5  # если что будем менять знак
#     e[i][i] = e[j][j] = c
#     e[i][j] = s
#     e[j][i] = s * -1
#     return e


def main():
    for i in range(N):
        with open(f'tests1/test{i}.txt', 'r') as file:
            matrix = [[int(x) for x in line.split()] for line in file]
        i, j = index_max_over_diag(matrix)
        e = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
        p = 2 * matrix[i][j]
        q = matrix[i][i] - matrix[j][j]
        d = (p ** 2 + q ** 2) ** 0.5
        if q != 0:
            r = abs(q) / (2 * d)
            c = (0.5 + r)
            s = (0.5 - r) ** 0.5 * sign(p * q) if q / p < 1000 else s = abs(p) * sign(p * q) / (2 * c * d)
        else:
            c = s = 2 ** 0.5 / 2
        b = deepcopy(matrix)
        b[i][i] = c ** 2 * matrix[i][j] + s ** 2 * matrix[j][j] + 2 * c * s * matrix[i][j]
        b[j][j] = s ** 2 * matrix[i][i] + c ** 2 * matrix[j][j] - 2 * c * s * matrix[i][j]
        b[i][j] = b[j][i] = 0
        for m in range(1, len(matrix)):
            b[i][m] = b[m][i] = c * matrix[m][i] + s * matrix[m][j]
            b[j][m] = b[m][j] = s * matrix[m][i] + c * matrix[m][j]




if __name__ == '__main__':
    main()
