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
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if matrix[i][j] > m:
                m = matrix[i][j]
                k, p = i, j
    return k, p


def get_max_over_diag(matrix):
    return max([max(a) for a in matrix])


def get_T(i, j, a):
    e = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    t = 2 * a[i][j] / (a[i][i] - a[i][j])
    c = (((1 + 1 / (1 + t)) ** 0.5) / 2) ** 0.5
    print(f'c = {c}')
    if 1 - 1 / (1 + t) < 0:
        print('da')
        s = ((((1 - 1 / (1 + t)) * (-1)) ** 0.5) / 2) ** 0.5
    else:
        s = (((1 - 1 / (1 + t)) ** 0.5) / 2) ** 0.5  # если что будем менять знак
    print(f's = {s}')
    e[i][i] = e[j][j] = c
    e[i][j] = s
    e[j][i] = s * -1
    return e


def main():
    for i in range(N):
        with open(f'tests1/test{i}.txt', 'r') as file:
            a = [[float(x) for x in line.split()] for line in file]
        _ = 0
        b = deepcopy(a)
        while get_max_over_diag(b) > EPS:
            i, j = index_max_over_diag(b)
            t = get_T(i, j, b)
            p = 2 * b[i][j]
            q = b[i][i] - b[j][j]
            d = (p ** 2 + q ** 2) ** 0.5
            if q != 0:
                r = abs(q) / (2 * d)
                c = (0.5 + r)
                if q / p < 1000:
                    s = (0.5 - r) ** 0.5 * sign(p * q)
                else:
                    s = abs(p) * sign(p * q) / (2 * c * d)
            else:
                c = s = 2 ** 0.5 / 2
            bk = deepcopy(b)
            bk[i][i] = c ** 2 * b[i][j] + s ** 2 * b[j][j] + 2 * c * s * b[i][j]
            bk[j][j] = s ** 2 * b[i][i] + c ** 2 * b[j][j] - 2 * c * s * b[i][j]
            bk[i][j] = b[j][i] = 0
            for m in range(1, len(b)):
                bk[i][m] = bk[m][i] = c * b[m][i] + s * b[m][j]
                bk[j][m] = bk[m][j] = s * b[m][i] + c * b[m][j]
            print(t)
            b = mul_matrix(mul_matrix(transpon(t), bk), t)
            print(_ + 1)
            _ += 1
        for i in range(len(b)):
            for j in range(len(b)):
                print(b[j][i])
            print()


if __name__ == '__main__':
    main()
