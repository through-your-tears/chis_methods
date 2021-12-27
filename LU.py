from fractions import Fraction
from copy import deepcopy


def LU(a):
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
    print()
    for row in u:
        print(*row)
    print()
    for row in l:
        print(*row)
    print()
    b = [Fraction(a[i][n]) for i in range(n)]
    if l[0][0] == 0:
        return
    y = [b[0] / l[0][0]]
    for i in range(1, n):
        s = 0
        for j in range(i):
            s += l[i][j] * y[j]
        if l[i][i] != 0:
            y.append((b[i] - s) / l[i][i])
        else:
            y.append(Fraction(0))
    if u[n-1][n-1] == 0:
        return
    x = [Fraction(0) for i in range(n)]
    x[n-1] = y[n-1] / u[n-1][n-1]
    for i in range(n-2, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += u[i][j] * x[j]
        if u[i][i] != 0:
            x[i] = (y[i] - s) / u[i][i]
        else:
            x[i] = 0
    return x


if __name__ == '__main__':
    p = int(input())
    matrix = [[Fraction(a) for a in input().split()] for i in range(p)]
    answer = LU(matrix)
    if answer is None:
        print('Нет решения')
    else:
        print(*answer, sep='\n')
