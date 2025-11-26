import time
from typing import Callable


def timeit_once(func: Callable, *args, **kwargs) -> tuple:
    start = time.perf_counter()
    res = func(*args, **kwargs)
    end = time.perf_counter()
    return res, end - start


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    res = {}
    for name, arr in arrays.items():
        res[name] = {}
        for name_alg, func_alg in algos.items():
            copy_arr = arr.copy()
            res[name][name_alg] = timeit_once(func_alg, copy_arr)[1]
    return res
