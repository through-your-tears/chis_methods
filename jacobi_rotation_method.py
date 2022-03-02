from LU_obr import mul_matrix
from obr_matrix import transpon, obr_matrix


EPS = 0.001
N = 4

"""Находим максимальный по модулю наддиагональный элемент, его i и j - строки, куда ставим cos и sin"""
def main():
    for i in range(N):
        with open(f'tests1/test{i}.txt', 'r') as file:
            matrix = [[int(x) for x in line.split()] for line in file]
            n = matrix[0][0]
            matrix.pop(0)


if __name__ == '__main__':
    main()
