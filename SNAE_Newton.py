from sympy import *
from copy import deepcopy
from LU_obr import mul_matrix


def gauss(a):
    n = len(a)
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
    ans = [float(0) for i in range(n-1)]
    ans.append(a[-1][-1] / a[-1][-2])
    for i in range(n-2, -1, -1):
        row_sum = 0
        for j in range(i+1, n):
            row_sum += a[i][j] * ans[j]
        ans[i] = (a[i][n] - row_sum) / a[i][i]
    return ans


def transpon(a):
    n = len(a)
    return [[a[j][i] for j in range(n)] for i in range(n)]


def sub_vectors(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result


def sub_matrix(a, b):
    result = []
    for i in range(len(a)):
        c = []
        for j in range(len(b)):
            c.append(a[i][j]-b[i][j])
        result.append(c)
    return result


def add_matrix(a, b):
    result = []
    for i in range(len(a)):
        c = []
        for j in range(len(b)):
            c.append(a[i][j]+b[i][j])
        result.append(c)
    return result


def mul_matrix_on_vector(mat, vec):
    result = []
    for i in range(len(mat)):
        s = 0
        for j in range(len(mat[i])):
            s += mat[i][j] * vec[j]
        result.append(s)
    return result


def main():
    eps = 0.01
    functions = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        for i in range(n):
            functions.append(parse_expr(lines[i+1], evaluate=False))
        v = [float(x) for x in lines[-1].split()]
    d = {f'x{j}': v[j] for j in range(n)}
    m = []
    va = []
    for i in range(n):
        va.append(functions[i].subs(d).evalf())
    for i in range(n):
        c = []
        for j in range(n):
            c.append(diff(functions[i], f'x{j}').subs(d).evalf())
        m.append(c)
    matrix = [[float(m[i][j]) for j in range(n)] for i in range(n)]
    a = obr_matrix(matrix)
    v1 = sub_vectors(v, mul_matrix_on_vector(a, va))
    while max([abs(x) for x in sub_vectors(v, v1)]) > eps:
        v = v1
        d = {f'x{j}': v[j] for j in range(n)}
        m = []
        va = []
        for i in range(n):
            va.append(functions[i].subs(d).evalf())
        for i in range(n):
            c = []
            for j in range(n):
                c.append(diff(functions[i], f'x{j}').subs(d).evalf())
            m.append(c)
        matrix = [[float(m[i][j]) for j in range(n)] for i in range(n)]
        a = obr_matrix(matrix)
        v1 = sub_vectors(v, mul_matrix_on_vector(a, va))
    print(v1)

    # va = []
    # for j in range(n):
    #     va.append(functions[j].subs(d).evalf())
    # u = obr_matrix(matrix)
    # e = [[float(1) if i == j else float(0) for i in range(n)] for j in range(n)]
    # v1 = sub_vectors(v, mul_matrix_on_vector(u, va))
    # try:
    #     while max([abs(x) for x in sub_vectors(v, v1)]) > eps:
    #         psi = sub_matrix(e, mul_matrix(matrix, u))
    #         u = add_matrix(u, mul_matrix(u, psi))
    #         v = v1
    #         d = {f'x{j}': v[j] for j in range(n)}
    #         va.clear()
    #         m = []
    #         for i in range(n):
    #             c = []
    #             for j in range(n):
    #                 c.append(diff(functions[i], f'x{j}').subs(d).evalf())
    #             m.append(c)
    #         matrix = [[float(m[i][j]) for j in range(n)] for i in range(n)]
    #         for j in range(n):
    #             va.append(functions[j].subs(d).evalf())
    #         v1 = sub_vectors(v, mul_matrix_on_vector(u, va))
    #     print(v1)
    # except TypeError:
    #     print('Неправильно задано начальное разбиение или нет корней')


if __name__ == '__main__':
    main()
