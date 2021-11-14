from fractions import Fraction


def LU_det(a):
    n = len(a)
    l = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    u = [[Fraction(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                s = 0
                for k in range(i - 1):
                    s += l[i][k] * u[k][j]
                u[i][j] = a[i][j] - s
            else:
                s = 0
                for k in range(j - 1):
                    s += l[i][k] * u[k][j]
                try:
                    l[i][j] = (a[i][j] - s) / u[j][j]
                except ZeroDivisionError:
                    l[i][j] = Fraction(0)
    for row in u:
        print(*row)
    print()
    for row in l:
        print(*row)


if __name__ == '__main__':
    p = int(input())
    matrix = [[Fraction(a) for a in input().split()] for i in range(p)]
    print(LU_det(matrix))