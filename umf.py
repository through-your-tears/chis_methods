from math import *

import openpyxl as xl


def start_cond(t):
    # return t ** 2
    return sin(2*pi*t)


def border_cond_sec(t):
    # return exp(t + 1)
    return t


def border_cond_first_der(t):
    return 0


def progonka(matrix):
    n = len(matrix)
    a = [-1 * matrix[0][1] / matrix[0][0]]
    b = [matrix[0][n] / matrix[0][0]]
    for i in range(1, n):
        y = matrix[i][i] + matrix[i][i - 1] * a[i - 1]
        a.append(-1 * matrix[i][i + 1] / y)
        b.append((matrix[i][n] - matrix[i][i - 1] * b[i - 1]) / y)
    b.append((matrix[n-1][n] - matrix[n-1][n-2] * b[n-2]) / (matrix[n-1][n-1] + matrix[n-1][n-2] * a[n-2]))
    x = [0 for i in range(len(matrix))]
    x[-1] = b[-1]
    for i in range(len(matrix)-2, -1, -1):
        x[i] = a[i] * x[i+1] + b[i]
    return x


def main():
    start_point = 0
    end_point = 1
    start_time = 1
    end_time = 4
    splitX = 20
    splitT = 30
    alpha = 0.1
    hX = (end_point - start_point) / splitX
    hT = (end_time - start_time) / splitT
    U_t_x = [[0 for j in range(splitX+1)] for i in range(splitT+1)]
    x = start_point
    curr_time = start_time
    for i in range(len(U_t_x[0])):
        U_t_x[0][i] = start_cond(x)
        x += hX
    for i in range(len(U_t_x)):
        U_t_x[i][splitX] = border_cond_sec(curr_time)
        curr_time += hT
    alphsq = alpha * alpha
    hXsq = hX * hX
    curr_time = start_time + hT
    tridig = [[0 for j in range(splitX+2)] for i in range(splitX+1)]
    tridig[0][0] = -1
    tridig[0][1] = 1
    tridig[0][-1] = border_cond_first_der(curr_time) * hT
    tridig[splitX][-1] = border_cond_sec(curr_time)
    tridig[-1][splitX - 1] = 0
    tridig[-1][splitX] = 1
    for i in range(1, splitX):
        tridig[i][i-1] = 1
        tridig[i][i] = -1 * (2 + hXsq / hT / alphsq)
        tridig[i][i+1] = 1
        tridig[i][-1] = -U_t_x[0][i] * hXsq / hT / alphsq
    U_t_x[1] = progonka(tridig)
    curr_time += hT
    for _ in range(2, splitT+1):
        alphsq = alpha * alpha
        hXsq = hX * hX
        tridig = [[0 for j in range(splitX + 2)] for i in range(splitX + 1)]
        tridig[0][0] = -1
        tridig[0][1] = 1
        tridig[0][-1] = border_cond_first_der(curr_time) * hT
        tridig[splitX][-1] = border_cond_sec(curr_time)
        tridig[-1][splitX - 1] = 0
        tridig[-1][splitX] = 1
        for i in range(1, splitX):
            tridig[i][i - 1] = 1
            tridig[i][i] = -1 * (2 + hXsq / hT / alphsq)
            tridig[i][i + 1] = 1
            tridig[i][-1] = -U_t_x[_-2][i] * hXsq / hT / alphsq
        U_t_x[_] = progonka(tridig)
        curr_time += hT
    wb = xl.Workbook('Answers.xls')
    wb.create_sheet('1')
    ws = wb['1']
    for row in U_t_x:
        ws.append(row)
    wb.save('Answers.xls')


if __name__ == '__main__':
    main()
