from math import *

import matplotlib.pyplot as plt

from gauss import gauss


def start_cond(t):
    # return t ** 2
    return 0


def border_cond_sec(t):
    # return exp(t + 1)
    return 10*sin(t)


def border_cond_first_der(t):
    return -abs(sin(t))


def main():
    N = 200
    M = 200
    a = 0
    alpha = 2
    b = 20
    t = 0
    T = 200
    hX = (b - a) / (M - 1)
    hT = (T - t) / (N - 1)
    u_tx = [[0 for i in range(M)] for j in range(N)]
    i, j = 0, a
    while j <= b:
        u_tx[0][i] = start_cond(j)
        j += hX
        i += 1
    i = 0
    ind = M - 1
    tm = t
    while tm < T:
        u_tx[i][ind] = border_cond_sec(tm)
        tm += hT
        i += 1
    Mind = M - 1
    curT = t
    # for row in u_tx:
    #     print(*row)
    # print()
    for ti in range(1, N):
        tridiag = [[0 for j in range(M+1)] for _ in range(M)]
        tridiag[0][0] = -1
        tridiag[0][1] = 1
        tridiag[0][M] = border_cond_first_der(curT) * hX
        tridiag[Mind][M-2] = 0
        tridiag[Mind][M-1] = 1
        tridiag[Mind][M] = border_cond_sec(curT) * hX
        for n in range(1, M - 1):
            tridiag[n][n-1] = - (alpha ** 2) / hX ** 2 * hT
            tridiag[n][n] = 2 * (alpha ** 2) / hX ** 2 * hT + 1
            tridiag[n][n+1] = - (alpha ** 2) / hX ** 2 * hT
            tridiag[n][M] = u_tx[ti - 1][n]
        u_tx[ti] = gauss(tridiag)
        curT += hX

    # for row in u_tx:
    #     print(*row)
    plt.imshow(u_tx, cmap='hot', interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    main()
