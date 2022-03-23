from math import sqrt


def euler(func, a, b, n, x, y):
    coords = {}
    h = (b - a) / n
    for i in range(n):
        y += h * func(x, y)
        x += h
        coords[str(x)] = y
    return coords


def adams(func, points, n, a, b):
    coords = {}
    return coords


def main():
    functions = [
        lambda x, y: (3 * y + 2 * x * y) / (x ** 2),
    ]
