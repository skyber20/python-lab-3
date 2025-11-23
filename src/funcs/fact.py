def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('Факториал определен только для целых чисел')
    if n < 0:
        raise ValueError('Факториал не определен для отрицательных чисел')

    if n <= 1:
        return 1

    res = 1
    for i in range(2, n + 1):
        res *= i

    return res


def factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('Факториал определен только для целых чисел')
    if n < 0:
        raise ValueError('Факториал не определен для отрицательных чисел')

    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

