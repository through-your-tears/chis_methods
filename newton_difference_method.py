from sympy import diff
from math import *


def main():
    inp = [float(a) for a in input().split()]
    x, a, b = inp
    func = input()
    code = compile(func, '<string', 'eval')
    eval(code)
    dfunc = diff(func)


if __name__ == '__main__':
    main()