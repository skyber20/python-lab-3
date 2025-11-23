def quick_sort(a: list[int | float]) -> list[int | float]:
    if not all(isinstance(i, (int, float)) for i in a):
        raise TypeError('На вход должен подаваться список чисел')

    def _quick_sort(arr: list[int | float]) -> list[int | float]:
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left_arr = [i for i in arr if i < pivot]
        middle = [i for i in arr if i == pivot]
        right_arr = [i for i in arr if i > pivot]

        return _quick_sort(left_arr) + middle + _quick_sort(right_arr)

    return _quick_sort(a)

