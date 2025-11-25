import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    if n <= 0 or lo > hi:
        return []

    if seed is not None:
        random.seed(seed)

    if distinct:
        if n > hi - lo + 1:
            raise ValueError(f'Невозможно сгенерировать {n} различных чисел в диапазоне [{lo}, {hi}]')
        return random.sample(range(lo, hi+1), n)
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if n <= 0:
        return []

    if seed is not None:
        random.seed(seed)

    lst = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        lst[i], lst[j] = lst[j], lst[i]

    return lst


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if n <= 0 or k_unique <= 0:
        return []

    if k_unique > n:
        k_unique = n

    if seed is not None:
        random.seed(seed)

    unique_values = random.sample(range(0, n+1), k_unique)
    return [random.choice(unique_values) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    if n <= 0:
        return []
    return list(range(n - 1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if n <= 0 or lo > hi:
        return []

    if seed is not None:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]
