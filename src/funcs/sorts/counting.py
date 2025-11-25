from typing import Callable


def counting_sort(a: list, key: Callable = None) -> list:
    if not a:
        return []

    key = key or (lambda x: x)

    try:
        transformed = [key(i) for i in a]

        if not all(isinstance(i, int) for i in transformed):
            raise TypeError('На вход должен подаваться список из целочисленных элементов')

        mn, mx = min(transformed), max(transformed)

        if mn == mx:
            return a

        counts = [[] for _ in range(mx - mn + 1)]

        for orig, transf in zip(a, transformed):
            counts[transf - mn].append(orig)

        res = []
        for elem in counts:
            res.extend(elem)
    except Exception:
        raise TypeError('key к данному типу не применим')

    return res
