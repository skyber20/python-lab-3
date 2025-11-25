from typing import Callable


def quick_sort(a: list, key: Callable = None, cmp: Callable = None) -> list:
    if len(a) <= 1:
        return a

    key = key or (lambda x: x)
    cmp = cmp or (lambda x, y: x > y)

    try:
        pivot = key(a[len(a) // 2])
        left_arr, middle, right_arr = [], [], []

        for elem in a:
            i = key(elem)
            if cmp(pivot, i):
                left_arr.append(elem)
            elif cmp(i, pivot):
                right_arr.append(elem)
            else:
                middle.append(elem)
    except Exception:
        raise TypeError('key или cmp к данному типу не применимы')

    return quick_sort(left_arr, key, cmp) + middle + quick_sort(right_arr, key, cmp)

