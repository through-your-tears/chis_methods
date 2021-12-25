from fractions import Fraction
from copy import deepcopy


def mul_matrix(a, b):
    try:
        rows_a = len(a)
    except Exception:
        rows_a = 1
    try:
        cols_a = len(a[0])
    except Exception:
        cols_a = 1
    try:
        rows_b = len(b)
    except Exception:
        rows_b = 1
    try:
        cols_b = len(b[0])
    except Exception:
        cols_b = 1
    if cols_a != rows_b:
        raise ValueError
    c = [[float(0) for row in range(cols_b)] for col in range(rows_a)]
    if cols_b != 1:
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    c[i][j] += a[i][k] * b[k][j]
    else:
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    c[i][j] += a[i][k] * b[k]
    return c


def diagonal_predominance(a):
    n = len(a)
    c = [a[j][n] for j in range(n)]
    d = [[1 if i != j else n + 1 for j in range(n)] for i in range(n)]
    aa = deepcopy([[a[i][j] for j in range(n)] for i in range(n)])
    matrix = mul_matrix(aa, d)
    b = mul_matrix(matrix, c)
    for i in range(n):
        matrix[i].append(*b[i])
    return matrix


def simple_iterations(a):
    n = len(a)
    matr = diagonal_predominance(a)
    c = [[(-1 * matr[i][j] / matr[i][i]) if i != j else float(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        c[i].append(matr[i][n] / matr[i][i])
    for row in c:
        print(*row)
    x = [c[j][n] for j in range(n)]
    xp = [0 for i in range(n)]
    while max([abs(xp[i]-x[i]) for i in range(n)]) > 0.001:
        print(x, xp)
        p = deepcopy(xp)
        for i in range(n):
            xp[i] = sum([x[j] * c[i][j] for j in range(n)])
            xp[i] += c[i][n]
        x = p
        print(xp, x)
        print(max([abs(xp[i] - x[i]) for i in range(n)]))
    return xp



def main():
    n = int(input())
    matrix = [[float(a) for a in input().split()] for i in range(n)]
    answer = simple_iterations(matrix)
    print('Ответ: ', *answer, sep='\n')


if __name__ == '__main__':
    main()