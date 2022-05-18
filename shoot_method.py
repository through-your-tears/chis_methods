from copy import deepcopy
from math import log

from matplotlib import pyplot as plt
import numpy as np

from five_steps_adams_method_SDU import Vector, adams


def shooting(functions, koshi_data_first, koshi_data_second, numeric_data, epsilons):
    first_shoot = adams(functions, koshi_data_first, epsilons)[-1][-1][-1]
    second_shoot = adams(functions, koshi_data_second, epsilons)[-1][-1][-1]
    first_shoot_f = first_shoot - numeric_data
    second_shoot_f = second_shoot - numeric_data
    koshi_data = (koshi_data_first[0], Vector([koshi_data_first[1][0], koshi_data_second[1][1] - (koshi_data_second[1][1] -
                  koshi_data_first[1][1]) * second_shoot_f / (second_shoot_f - first_shoot_f)]), koshi_data_first[-1])
    return adams(functions, koshi_data, epsilons)


def main():
    functions = (
        (
            lambda t, y: y[1],
            lambda t, y: ((2 * t + 4) * y[1] - 2 * y[0]) / (t * (t + 4))
        ),
        (
            lambda t, y: y[1],
            lambda t, y: (6 * t - 4 * t * y[1] - 2 * y[0]) / (t ** 2 - 1)
        ),
        (
            lambda t, y: y[1],
            lambda t, y: (t + 1 / t - (t + 2) * y[1] + y[0]) / (t * (t + 1))
        ),
    )
    anal_functions = (
        lambda x: 0.5 * (x + 2) - 0.2 * x * x,
        lambda x: 10 / (x + 1) + 5 / (x - 1) + x,
        lambda x: 0.2 * (x + 2) + 10 / x + (x / 2 + 1) * log(abs(x)) + 1.5
    )
    koshi_data_first = (
        (0.5, Vector([1.2, 0.1]), 3.51),
        (-8, Vector([-9.984126, 0.1]), -2.99),
        (1, Vector([12.1, 0.1]), 7.01)
    )
    koshi_data_second = (
        (0.5, Vector([1.2, 0.5]), 3.51),
        (-8, Vector([-9.984126, 0.5]), -2.99),
        (1, Vector([12.1, 0.5]), 7.01)
    )
    numeric_data = (
        -0.9,
        -1.8125,
        1.61173058
    )
    epsilons = (
        0.12,
        0.26,
        0.12
    )
    for i in range(len(koshi_data_first)):
        graph_coords = shooting(functions[i], koshi_data_first[i], koshi_data_second[i], numeric_data[i], epsilons[i])
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords]),
                 np.array([deepcopy(a[1][0]) for a in graph_coords]), label=f'h = {epsilons[i]}')
        graph_coords_any = shooting(functions[i], koshi_data_first[i], koshi_data_second[i], numeric_data[i],
                                    epsilons[i] / 2)
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([deepcopy(a[1][0]) for a in graph_coords_any]), label=f'h = {epsilons[i] / 2}')
        plt.plot(np.array([deepcopy(a[0]) for a in graph_coords_any]),
                 np.array([anal_functions[i](deepcopy(a[0])) for a in graph_coords_any]), label='Точное')
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()
