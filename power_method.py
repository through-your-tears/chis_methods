from SNAE_Newton import mul_matrix_on_vector


def normalize(a: list) -> list:
    return [x / (sum([y**2 for y in a])**0.5) for x in a]


def main():
    n = int(input())
    matrix = [[float(x) for x in input().split()] for i in range(n)]
    y = [float(x) for x in input().split()]
    x = normalize(y)
    delta = 0.001
    yk = mul_matrix_on_vector(matrix, x)
    xk = normalize(yk)
    lmbd = [0.1 for i in range(n)]
    lmbdk = [yk[i] / x[i] for i in range(n)]
    eps = 0.00001
    while max([lmbdk[i] - lmbd[i] for i in range(n)]) > eps:
        y, x = yk, xk
        yk = mul_matrix_on_vector(matrix, x)
        xk = normalize(yk)
        lmbd = lmbdk
        lmbdk = [yk[i] / x[i] if abs(x[i]) > delta else lmbd[i] for i in range(n)]
    print(sum(lmbdk) / n, xk)


if __name__ == '__main__':
    main()
