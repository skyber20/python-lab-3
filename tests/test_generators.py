import pytest
from src.generators.genetators import rand_int_array, rand_float_array, nearly_sorted, reverse_sorted, many_duplicates


def test_empty_generators():
    assert rand_int_array(-1, lo=0, hi=100) == []
    assert rand_int_array(3, lo=100, hi=0) == []

    assert rand_float_array(-1) == []
    assert rand_float_array(3, lo=1.0, hi=0.0) == []

    assert nearly_sorted(-1, 2) == []

    assert many_duplicates(-1) == []
    assert many_duplicates(3, k_unique=-2) == []

    assert reverse_sorted(-3) == []


def test_generators_seed():
    assert rand_int_array(3, 0, 100, seed=20) == rand_int_array(3, 0, 100, seed=20)
    assert rand_float_array(20, seed=45) == rand_float_array(20, seed=45)
    assert nearly_sorted(15, 3, seed=52) == nearly_sorted(15, 3, seed=52)
    assert many_duplicates(23, seed=128) == many_duplicates(23, seed=128)


def test_distinct():
    data = rand_int_array(100, 0, 150, distinct=True)
    assert len(set(data)) == len(data)


def test_distinct_error():
    with pytest.raises(ValueError):
        assert rand_int_array(100, 0, 25, distinct=True)
