from numpy import*


def jacobian(f, x):
    h = 1.0e-4
    n = len(x)
    Jac = zeros([n, n])
    f0 = f(x)
    for i in arange(0, n, 1):
        tt = x[i]
        x[i] = tt + h
        f1 = f(x)
        x[i] = tt
        Jac[:, i] = (f1 - f0)/h
    return Jac, f0


def newton(f, x, tol=0.001):
    global n
    iterMax = 50
    for i in range(iterMax):
        Jac, fO = jacobian(f, x)
        if sqrt(dot(fO, fO) / len(x)) < tol:
            return x, i
        dx = linalg.solve(Jac, fO)
        x = x - dx
    print("Too many iterations for the Newton method")


def f(x):
    global n
    f = zeros([n])
    for i in arange(0, n-1, 1):
        f[i] = (3 + 2*x[i])*x[i] - x[i-1] - 2*x[i+1] - 2
    f[0] = (3 + 2*x[0])*x[0] - 2*x[1] - 3
    f[n-1] = (3 + 2*x[n-1])*x[n-1] - x[n-2] - 4
    return f


def main():
    global n
    n = int(input())
    x0 = zeros([n])
    x, iter = newton(f, x0)
    print('Solution:\n', x)


if __name__ == '__main__':
    main()
