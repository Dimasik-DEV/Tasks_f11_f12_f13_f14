# Задача 1.3. Реализовать итерационную функцию (Вариант 30).

def func(n, m):
    res_1 = 0
    res_2 = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res_1 += i ** 5 - 48 * j ** 6
            res_2 += 85 * j + j ** 6 + 25

    return 69 * (res_1 + res_2)


def out(n, m):
    print('f(', n, ',', m, ') = %.2e' % func(n, m), sep='')


out(41, 37)
out(28, 52)
