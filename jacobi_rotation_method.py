from copy import deepcopy
from math import copysign

from LU_obr import mul_matrix


EPS = 0.001
N = 4


def sign(x):
    return copysign(1, x)


def index_max_over_diag(matrix):
    n = len(matrix)
    m = abs(matrix[0][1])
    k, p = 0, 1
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if abs(matrix[i][j]) > m:
                m = abs(matrix[i][j])
                k, p = i, j
    return k, p


def get_max_over_diag(matrix):
    n = len(matrix)
    m = abs(matrix[0][1])
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if abs(matrix[i][j]) > m:
                m = abs(matrix[i][j])
    return m


def main():
    for _ in range(N):
        print(f'Тест номер {_ + 1}')
        with open(f'tests1/test{_}.txt', 'r') as file:
            a = [[float(x) for x in line.split()] for line in file]
        b = deepcopy(a)
        tt = []
        while get_max_over_diag(b) > EPS:
            i, j = index_max_over_diag(b)
            e = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
            p = 2 * b[i][j]
            q = b[i][i] - b[j][j]
            d = (p ** 2 + q ** 2) ** 0.5
            if q != 0:
                r = abs(q) / (2 * d)
                c = (0.5 + r) ** 0.5
                if abs(q) / abs(p) < 1000000000000:
                    s = ((0.5 - r) ** 0.5) * sign(p * q)
                else:
                    s = abs(p) * sign(p * q) / (2 * c * d)
            else:
                c = s = (2 ** 0.5) / 2
            e[i][i] = e[j][j] = c
            e[j][i] = s
            e[i][j] = s * -1
            tt.append(e)
            bk = deepcopy(b)
            bk[i][i] = c ** 2 * b[i][i] + s ** 2 * b[j][j] + 2 * c * s * b[i][j]
            bk[j][j] = s ** 2 * b[i][i] + c ** 2 * b[j][j] - 2 * c * s * b[i][j]
            bk[i][j] = bk[j][i] = (c ** 2 - s ** 2) * b[i][j] + c * s * (b[j][j] - b[i][i])
            # bk[i][j] = bk[j][i] = 0
            for m in range(0, len(b)):
                if i != m and j != m:
                    bk[i][m] = bk[m][i] = c * b[m][i] + s * b[m][j]
                    bk[j][m] = bk[m][j] = -1 * s * b[m][i] + c * b[m][j]
            b = bk
        print('Собственные числа: ')
        for i in range(len(b)):
            print(b[i][i])
        e = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
        for i in range(len(tt)):
            e = mul_matrix(e, tt[i])
        print('Собственные вектора: ')
        # for i in range(len(e)):
        #     for j in range(len(e)):
        #         print(e[j][i], end=' ')
        #     print()
        for x in e:
            print(*x)


if __name__ == '__main__':
    main()
