from math import *


def derivate(func, x, xn):
    b = eval(func)
    x, xn = xn, x
    a = eval(func)
    return (a - b) / (x - xn)


def newton(func, a, b, eps=0.001):
    x = (b + a) / 2
    xn = x - eval(func) / derivate(func, x, x - 0.000000001)
    while abs(xn - x) > eps and xn >= a:
        xp = xn
        xn = xn - eval(func) / derivate(func, x, xn)
        x = xp
    return xn


def main():
    inp = [float(a) for a in input().split()]
    a, b, eps, eps1 = inp
    func = input()
    ans = []
    y = a
    while y < b:
        x = y
        f1 = eval(func)
        x += eps1
        f2 = eval(func)
        if abs(f1) < eps:
            ans.append(x)
        elif f1 * f2 < 0:
            ans.append(newton(func, y, x, eps))
        y += eps1
    if len(ans) != 0:
        print(*ans, sep='\n')
    else:
        print('На данном промежутке корни не найдены!!!')


if __name__ == '__main__':
    main()
