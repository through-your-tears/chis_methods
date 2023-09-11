from random import randint
from SNAE_Newton import mul_matrix_on_vector


N = 4
DELTA = 0.001
EPS = 0.000000001


def vec_length(a: list) -> float:
    return sum([y**2 for y in a])**0.5


def normalize(a: list) -> list:
    return [x / vec_length(a) for x in a]


def power_method(matrix):
    n = len(matrix)
    y = [randint(0, 10000) for j in range(n)]
    x = normalize(y)
    yk = mul_matrix_on_vector(matrix, x)
    xk = normalize(yk)
    lmbd = [1 for i in range(n)]
    lmbdk = [yk[i] / x[i] for i in range(n)]
    flags = [True if abs(x[i]) > DELTA else False for i in range(n)]
    while max([(lmbdk[i] - lmbd[i]) ** 2 for i in range(n)]) ** 0.5 > EPS:
        x = xk
        yk = mul_matrix_on_vector(matrix, x)
        xk = normalize(yk)
        lmbd = lmbdk
        flags = [True if abs(x[i]) > DELTA else False for i in range(n)]
        lmbdk = [yk[i] / x[i] if abs(x[i]) > DELTA else lmbd[i] for i in range(n)]
        ans = [lmbdk[i] for i in range(n) if flags[i]]
    return sum(ans) / len(ans), xk


def main():
    for i in range(N):
        with open(f'tests0/test{i}.txt', 'r') as file:
            matrix = [[int(x) for x in line.split()] for line in file]
            n = matrix[0][0]
            matrix.pop(0)
        y = [randint(0, 10000) for j in range(n)]
        x = normalize(y)
        yk = mul_matrix_on_vector(matrix, x)
        xk = normalize(yk)
        lmbd = [1 for i in range(n)]
        lmbdk = [yk[i] / x[i] for i in range(n)]
        flags = [True if abs(x[i]) > DELTA else False for i in range(n)]
        while max([(lmbdk[i] - lmbd[i])**2 for i in range(n)])**0.5 > EPS:
            x = xk
            yk = mul_matrix_on_vector(matrix, x)
            xk = normalize(yk)
            lmbd = lmbdk
            flags = [True if abs(x[i]) > DELTA else False for i in range(n)]
            lmbdk = [yk[i] / x[i] if abs(x[i]) > DELTA else lmbd[i] for i in range(n)]
            ans = [lmbdk[i] for i in range(n) if flags[i]]
        print(f'Ответ на тест{i}: {sum(ans) / len(ans)}, {xk}')
        with open(f'tests0/answer{i}.txt', 'r') as f:
            print(f'проверка из файла с ответами: {f.readline()}')


if __name__ == '__main__':
    main()
