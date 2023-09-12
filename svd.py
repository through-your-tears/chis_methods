from math import sqrt

from LU_obr import mul_matrix
from obr_matrix import transpon
from power_method import power_method
from jacobi_rotation_method import jacobi_rotation
from numpy import linalg


N = 3


def svd(matrix):
    if len(matrix) < len(matrix[0]):
        matrix = transpon(matrix)
    k = min(len(matrix), len(matrix[0]))
    res, any_res = jacobi_rotation(mul_matrix(matrix, transpon(matrix))), jacobi_rotation(
        mul_matrix(transpon(matrix), matrix))
    tr = transpon(res[1])
    dict_res = {res[0][i]: tr[i] for i in range(len(res[0]))}
    s = sorted(dict_res.keys())[-k:]
    any_tr = transpon(any_res[1])
    dict_any_res = {any_res[0][i]: any_tr[i] for i in range(len(any_res[0]))}
    any_s = sorted(dict_any_res.keys())
    answers_dict = {
        'S': list(map(sqrt, s)),
        'U': transpon([dict_res[x] for x in s]),
        'V': [dict_any_res[x] for x in any_s]
    }
    return answers_dict


def main():
    for i in range(N):
        print(f'Тест {i+1}')
        with open(f'tests_svd/test{i}.txt', 'r') as file:
            matrix = [[float(x) for x in line.split()] for line in file]
        res = svd(matrix)
        print('сингулярные числа: ')
        print(res['S'])
        print('матрица U: ')
        print(*res['U'], sep='\n')
        print('матрица V: ')
        print(*res['V'], sep='\n')
        print('numpy method')
        print(linalg.svd(matrix))
        print()


if __name__ == '__main__':
    main()
