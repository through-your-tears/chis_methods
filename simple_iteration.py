from fractions import Fraction
from copy import deepcopy


def simple_iterations(a):
    n = len(a)
    c = [[(-1 * a[i][j] / a[i][i]) if i != j else float(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        c[i].append(a[i][n] / a[i][i])
    x = [c[j][n] for j in range(n)]
    xp = [0 for i in range(n)]
    while max([abs(xp[i]-x[i]) for i in range(n)]) > 0.001:
        p = deepcopy(xp)
        for i in range(n):
            xp[i] = sum([x[j] * c[i][j] for j in range(n)])
            xp[i] += c[i][n]
        x = p
    return xp


def main():
    n = int(input())
    matrix = [[float(a) for a in input().split()] for i in range(n)]
    answer = simple_iterations(matrix)
    print('Ответ: ', *answer, sep='\n')


if __name__ == '__main__':
    main()