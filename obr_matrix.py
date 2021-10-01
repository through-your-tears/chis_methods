from fractions import Fraction
from gauss import gauss
from copy import deepcopy


def transpon(a):
    return [[a[j][i] for j in range(n)] for i in range(n)]


def obr_matrix(m):
    ao = []
    n = len(m)
    e = [[Fraction(1) if i == j else Fraction(0) for i in range(n)] for j in range(n)]
    for i in range(n):
        a = deepcopy(m)
        for j in range(n):
            a[j].append(e[i][j])
        ao.append(gauss(a))
        for row in a:
            row.pop()
    return transpon(ao)


n = int(input())
matrix = [[Fraction(a) for a in input().split()] for i in range(n)]
answer = obr_matrix(matrix)
for row in answer:
    print(*row)
