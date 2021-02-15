# Задача 1.4. Реализовать рекуррентную функцию (Вариант 30).

import math


def f14(n):
    if n == 0:
        return 7

    return math.tan(f14(n - 1)) + abs(f14(n - 1))


print('%.2e' % f14(14))
print('%.2e' % f14(12))
