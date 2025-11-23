def count_digits(a: int, base: int) -> int:
    if a == 0:
        return 1
    cnt = 0
    while a:
        cnt += 1
        a //= base
    return cnt


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not all(isinstance(i, int) for i in a):
        raise TypeError('На вход должен подаваться список из целочисленных элементов')
    if not all(i >= 0 for i in a):
        raise ValueError('Все числа должны быть неотрицательными')
    if not isinstance(base, int):
        raise TypeError('Основание системы должно быть целочисленным')
    if base < 2:
        raise ValueError('Основание системы должно быть >= 2')
    if len(a) <= 1:
        return a

    mx = max(a)
    mx_digit = count_digits(mx, base)

    for i in range(1, mx_digit + 1):
        bucket = [[] for _ in range(base)]

        for elem in a:
            remainder = (elem // (base ** (i - 1))) % base
            bucket[remainder].append(elem)
        a = [j for elem in bucket for j in elem]

    return a
