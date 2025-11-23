def max_heapify(a: list[int | float], size: int, i: int) -> None:
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < size and a[l] > a[largest]:
        largest = l

    if r < size and a[r] > a[largest]:
        largest = r

    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, size, largest)


def build_max_heap(a: list[int | float]) -> None:
    size = len(a)
    for i in range(size // 2 - 1, -1, -1):
        max_heapify(a, size, i)


def heap_sort(a: list[int | float]) -> list[int | float]:
    if not a:
        return []
    if not all(isinstance(i, (int, float)) for i in a):
        raise TypeError('На вход должен подаваться список из чисел')

    build_max_heap(a)

    size = len(a)

    for i in range(size - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        size -= 1
        max_heapify(a, size, 0)

    return a
