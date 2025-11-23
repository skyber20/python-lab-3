def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    if not all(isinstance(i, int) for i in a):
        raise TypeError('На вход должен подаваться список из целочисленных элементов')

    mn, mx = min(a), max(a)
    counts = [0] * (mx - mn + 1)

    for i in a:
        counts[i-mn] += 1

    sorted_a = []
    for num, cnt in enumerate(counts, start=mn):
        sorted_a.extend([num] * cnt)
    return sorted_a
