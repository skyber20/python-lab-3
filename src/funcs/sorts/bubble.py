from typing import Callable


def bubble_sort(a: list, key: Callable = None, cmp: Callable = None) -> list:
    if not a:
        return []

    key = key or (lambda x: x)
    cmp = cmp or (lambda x, y: x > y)

    while True:
        swapped = False
        for i in range(len(a) - 1):
            try:
                if cmp(key(a[i]), key(a[i+1])):
                    a[i], a[i+1] = a[i+1], a[i]
                    swapped = True
            except Exception:
                raise TypeError('key или cmp к данному типу не применимы')
        if not swapped:
            break
    return a
