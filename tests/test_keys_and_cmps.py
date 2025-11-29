import pytest
from functools import cmp_to_key
from src import bubble_sort, quick_sort, heap_sort
from src.exceptions import KeyAndCmpAreBothUsed

test_key_data = [
        [('a', 3), ('b', 1), ('c', 2)],  # по второму элементу
        [{'x': 5}, {'x': 1}, {'x': 3}],   # по ключу
        ['apple', 'banana', 'pear'],    # длина
        [5, -2, 10, -8],                 # abs
    ]

key_funcs = [
    lambda x: x[1],
    lambda x: x['x'],
    lambda x: len(x),
    lambda x: abs(x)
]

test_cmp_data = [
    [5, 2, 8, 1, 9],
    ['a', 'ccc', 'bb'],
    [('b', 2), ('a', 1), ('c', 3)]
]

cmp_funcs = [
    lambda x, y: 1 if x < y else (-1 if x > y else 0),      # в порядке убывания
    lambda x, y: -1 if len(x) < len(y) else (1 if len(x) > len(y) else 0),   # по длине в порядке возрастания
    lambda x, y: -1 if x[1] < y[1] else (1 if x[1] > y[1] else 0)   # по второму элементу кортежа
]


@pytest.mark.parametrize('func', [bubble_sort, quick_sort, heap_sort])
@pytest.mark.parametrize('data,key_func', list(zip(test_key_data, key_funcs)))
def test_key_funcs(func, data, key_func):
    assert func(data, key=key_func) == sorted(data, key=key_func)


@pytest.mark.parametrize('func', [bubble_sort, quick_sort, heap_sort])
@pytest.mark.parametrize('data,cmp_func', list(zip(test_cmp_data, cmp_funcs)))
def test_cmp_funcs(func, data, cmp_func):
    assert func(data, cmp=cmp_func) == sorted(data, key=cmp_to_key(cmp_func))


@pytest.mark.parametrize('func', [bubble_sort, quick_sort, heap_sort])
def test_key_and_cmp_error(func):
    with pytest.raises(KeyAndCmpAreBothUsed):
        assert func([5, 2, 8, 1, 9], key=lambda x: -x, cmp=lambda x, y: 1 if x < y else (-1 if x > y else 0))

    with pytest.raises(TypeError):
        assert func([5, 2, 8, 1, 9], key=lambda x: len(x))
