from typing import Callable, Any, TypeVar
from functools import cmp_to_key
from src.exceptions import KeyAndCmpAreBothUsed

T = TypeVar('T')


def max_heapify(a: list[T], size: int, i: int, key: Callable[[T], Any]) -> None:
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < size and key(a[l]) > key(a[largest]):
        largest = l

    if r < size and key(a[r]) > key(a[largest]):
        largest = r

    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, size, largest, key)


def build_max_heap(a: list[T], key: Callable[[T], Any]) -> None:
    size = len(a)
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(a, size, i, key)


def heap_sort(
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

    arr = a.copy()
    size = len(arr)

    try:
        build_max_heap(arr, key)

        for i in range(size - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            size -= 1
            max_heapify(arr, size, 0, key)

        return arr
    except TypeError:
        raise TypeError('key к данному типу не применим')
