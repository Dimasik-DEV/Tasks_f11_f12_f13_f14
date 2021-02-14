# Задача 1.4. Реализовать рекуррентную функцию (Вариант 30).

import math


def func(n):
    if n == 0:
        return 7

    return math.tan(func(n - 1)) + abs(func(n - 1))


def out(n):
    print('f(', n, ') = %.2e' % func(n), sep='')


out(14)
out(12)
