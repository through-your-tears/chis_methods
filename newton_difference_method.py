from math import *


def derivate(func, x, xn):
    return (eval(func, {'x': xn}) - eval(func, {'x': x})) / (xn - x)


def newton(func, a, b, ans):
    x = b
    xn = eval(func) / derivate(func, x, x - 0.01)
    while abs(xn - x) > 0.001 and xn >= a:
        xp = xn
        xn = x - eval(func, {'x': x}) / derivate(func, x, xn)
        x = xp
    ans.append(xn)
    if xn <= b:
        newton(func, xn + 0.01, a, ans)
    return ans


def main():
    inp = [float(a) for a in input().split()]
    a, b = inp
    func = input()
    ans = []
    print(newton(func, a, b, ans))


if __name__ == '__main__':
    main()
