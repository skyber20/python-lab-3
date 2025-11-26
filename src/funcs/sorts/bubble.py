from typing import Callable


def bubble_sort(a: list, key: Callable = None, cmp: Callable = None) -> list:
    if not a:
        return []

    key = key or (lambda x: x)
    cmp = cmp or (lambda x, y: x > y)

    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - i - 1):
            try:
                if cmp(key(a[j]), key(a[j+1])):
                    a[j], a[j+1] = a[j+1], a[j]
                    swapped = True
            except Exception:
                raise TypeError('key или cmp к данному типу не применимы')
        if not swapped:
            break
    return a
