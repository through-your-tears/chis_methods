from math import *


def newton(func, a, b):
    x = a
    xi = eval(func)
    xn =
    while abs(xn - xi) < 0.001:



def main():
    inp = [float(a) for a in input().split()]
    a, b = inp
    func = input()
    print(newton(func, a, b))


if __name__ == '__main__':
    main()
