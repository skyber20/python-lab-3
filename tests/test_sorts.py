import pytest
import random
from src.constants import ALL_SORTS, FLOAT_SORTS
from src.generators.genetators import rand_int_array, nearly_sorted, reverse_sorted, many_duplicates, rand_float_array


@pytest.mark.repeat(5)
@pytest.mark.parametrize('func', ALL_SORTS)
def test_sort_funcs(func):
    n = random.randint(1, 250)

    data = rand_int_array(n, 1, 1000)
    assert func(data) == sorted(data)

    data = nearly_sorted(n, 10)
    assert func(data) == sorted(data)

    data = reverse_sorted(n)
    assert func(data) == sorted(data)

    data = many_duplicates(n, 15)
    assert func(data) == sorted(data)


@pytest.mark.repeat(5)
@pytest.mark.parametrize('func', FLOAT_SORTS)
def test_float_sort_funcs(func):
    n = random.randint(1, 250)

    data = rand_float_array(n, 0.0, 1000.0)
    assert func(data) == sorted(data)
