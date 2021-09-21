from fractions import Fraction


def gauss(a):
    for k in range(n):
        for i in range(k, n - 1):
            c = k
            while a[k][k] == 0 and c < n:
                if a[c][k] != 0:
                    a[c], a[k] = a[k], a[c]
                c += 1
            if a[k][k] == 0:
                return
            try:
                b = a[k][k] / a[i + 1][k]
                for j in range(k, n + 1):
                    a[i + 1][j] = a[i + 1][j] * b - a[k][j]
            except ZeroDivisionError:
                pass
    if a[n - 1][n - 1] == 0:
        return
    ans = [Fraction(0) for i in range(n-1)]
    ans.append(a[-1][-1] / a[-1][-2])
    for i in range(n-2, -1, -1):
        row_sum = 0
        for j in range(i+1, n):
            row_sum += a[i][j] * ans[j]
        ans[i] = (a[i][n] - row_sum) / a[i][i]
    return ans


n = int(input())
matrix = [[Fraction(a) for a in input().split()] for i in range(n)]
answer = gauss(matrix)
if answer is not None:
    print('Ответ: ', *answer, sep='\n')
else:
    print('Решений нет или бесконечно много')
