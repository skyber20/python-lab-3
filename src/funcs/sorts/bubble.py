from typing import Callable, TypeVar, Any
from functools import cmp_to_key
from src.exceptions import KeyAndCmpAreBothUsed

T = TypeVar('T')


def bubble_sort(
        a: list[T],
        key: Callable[[T], Any] | None = None,
        cmp: Callable[[T, T], int] | None = None) -> list[T]:
    if key is not None and cmp is not None:
        raise KeyAndCmpAreBothUsed()
    if not a:
        return []

    if cmp is not None:
        key = cmp_to_key(cmp)

    if key is None:
        key = lambda x: x

    try:
        for i in range(len(a) - 1):
            swapped = False
            for j in range(len(a) - i - 1):
                if key(a[j]) > key(a[j+1]):
                    a[j], a[j+1] = a[j+1], a[j]
                    swapped = True
            if not swapped:
                break
    except TypeError:
        raise TypeError('key к данному типу не применимы')
    return a
