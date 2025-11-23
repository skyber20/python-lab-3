def fibo(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('Последовательность Фибоначчи определена только для целых чисел')
    if n < 0:
        raise ValueError('Последовательность Фибоначчи не определена на отрицательных числах')

    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('Последовательность Фибоначчи определена только для целых чисел')
    if n < 0:
        raise ValueError('Последовательность Фибоначчи не определена на отрицательных числах')

    if n <= 1:
        return n

    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
