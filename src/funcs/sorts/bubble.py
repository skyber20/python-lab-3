def bubble_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    if not all(isinstance(i, int) for i in a):
        raise TypeError('На вход должен подаваться список из целочисленных элементов')

    while True:
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break
    return a
