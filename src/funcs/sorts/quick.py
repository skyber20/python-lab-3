from typing import Callable, Any, TypeVar
from functools import cmp_to_key
from src.exceptions import KeyAndCmpAreBothUsed

T = TypeVar('T')


def quick_sort(
        a: list[T],
        key: Callable[[T], Any] | None = None,
        cmp: Callable[[T, T], int] | None = None) -> list[T]:
    if key is not None and cmp is not None:
        raise KeyAndCmpAreBothUsed()
    if len(a) <= 1:
        return a

    if cmp is not None:
        key = cmp_to_key(cmp)

    if key is None:
        key = lambda x: x

    try:
        pivot = a[len(a) // 2]
        left_arr, middle, right_arr = [], [], []

        for i in a:
            if key(i) < key(pivot):
                left_arr.append(i)
            elif key(i) > key(pivot):
                right_arr.append(i)
            else:
                middle.append(i)
    except TypeError:
        raise TypeError('key к данному типу не применимы')

    return quick_sort(left_arr, key, cmp) + middle + quick_sort(right_arr, key, cmp)
