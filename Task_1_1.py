# Задача 1.1. Реализовать функцию (Вариант 30).

import math


def func(x):
    f = x ** 5 - x ** 6 - math.sqrt((12 * x ** 6 - 40 * x + 73) / (x ** 5 - x ** 7 + 45)) - (x ** 7 + 16 * x ** 6)
    return f


def out(x):
    print('f(', x, ') = %.2e' % func(x), sep='')


out(-17)
out(0)
