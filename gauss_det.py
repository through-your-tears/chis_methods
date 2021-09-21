from fractions import Fraction


def det(a):
    d = Fraction(1)
    for k in range(n):
        for i in range(k, n - 1):
            c = k
            while a[k][k] == 0 and c < n:
                if a[c][k] != 0:
                    a[c], a[k] = a[k], a[c]
                c += 1
            if a[k][k] == 0:
                return 0
            try:
                b = a[k][k] / a[i + 1][k]
                d *= 1 / b
                for j in range(k, n):
                    a[i + 1][j] = a[i + 1][j] * b - a[k][j]
            except ZeroDivisionError:
                pass
    if a[n - 1][n - 1] == 0:
        return 0
    for i in range(n):
        d *= a[i][i]
    return d


n = int(input())
matrix = [[Fraction(a) for a in input().split()] for i in range(n)]
print(det(matrix))
