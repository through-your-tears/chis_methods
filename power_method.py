from SNAE_Newton import mul_matrix_on_vector


def normalize(a: list) -> list:
    return [x / (sum([y**2 for y in a])**0.5) for x in a]


def main():
    N = 3
    for i in range(N):
        with open(f'tests0/test{i}.txt', 'r') as file:
            matrix = [[int(x) for x in line.split()] for line in file]
            n = matrix[0][0]
            matrix.pop(0)
        y = [float(1) for x in range(n)]
        x = normalize(y)
        delta = 0.001
        yk = mul_matrix_on_vector(matrix, x)
        xk = normalize(yk)
        lmbd = [0.1 for i in range(n)]
        lmbdk = [yk[i] / x[i] for i in range(n)]
        eps = 0.000000001
        while max([lmbdk[i] - lmbd[i] for i in range(n)]) > eps:
            y, x = yk, xk
            yk = mul_matrix_on_vector(matrix, x)
            xk = normalize(yk)
            lmbd = lmbdk
            lmbdk = [yk[i] / x[i] if abs(x[i]) > delta else lmbd[i] for i in range(n)]
        print(f'Ответ на тест{i}: {sum(lmbdk) / n}, {xk}')
        with open(f'tests0/answer{i}.txt', 'r') as f:
            print(f'проверка из файла с ответами: {f.readline()}')


if __name__ == '__main__':
    main()
