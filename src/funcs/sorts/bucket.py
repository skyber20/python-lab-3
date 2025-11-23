from src.funcs.sorts.quick import quick_sort


def bucket_sort(a: list[float | int], buckets: int | None = None) -> list[int| float]:
    if not a:
        return []
    if not all(isinstance(i, (int, float)) for i in a):
        raise TypeError('На вход должен подаваться список из чисел')

    if buckets is None:
        buckets = len(a)
    elif buckets <= 0:
        raise ValueError('buckets должно быть >= 1')

    mn, mx = min(a), max(a)
    if mn == mx:
        return a

    normalized_values = [(i - mn) / (mx - mn) for i in a]
    buckets_list = [[] for _ in range(buckets)]

    for orig_val, norm_val in zip(a, normalized_values):
        ind_bucket = int(norm_val * buckets)
        if ind_bucket == buckets:
            ind_bucket -= 1
        buckets_list[ind_bucket].append(orig_val)

    res_lst = []
    for bucket in buckets_list:
        res_lst.extend(quick_sort(bucket))

    return res_lst
