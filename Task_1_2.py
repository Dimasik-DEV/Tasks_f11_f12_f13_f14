# Задача 1.2. Реализовать кусочно-линейную функцию (Вариант 30).

def func(x):
    if x < 73:
        f = x ** 5 - x ** 6
    elif 73 <= x < 115:
        f = 12 * x ** 6 - 40 * x + 73
    else:
        f = x ** 5 - x ** 7 + 45
    return f


def out(x):
    print('f(', x, ') = %.2e' % func(x), sep='')


out(47)
out(42)