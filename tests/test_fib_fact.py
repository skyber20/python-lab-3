import pytest
from src import fibo, fibo_recursive, factorial, factorial_recursive


def test_fib():
    assert fibo(0) == fibo_recursive(0) == 0
    assert fibo(2) == fibo_recursive(2) == 1
    assert fibo(3) == fibo_recursive(3) == 2
    assert fibo(4) == fibo_recursive(4) == 3
    assert fibo(7) == fibo_recursive(7) == 13

    with pytest.raises(ValueError):
        assert fibo(-1)

    with pytest.raises(ValueError):
        assert fibo_recursive(-1)

    with pytest.raises(TypeError):
        assert fibo('fdwef')

    with pytest.raises(TypeError):
        assert fibo_recursive('fdwef')


def test_fact():
    assert factorial(0) == factorial_recursive(0) == 1
    assert factorial(1) == factorial_recursive(1) == 1
    assert factorial(5) == factorial_recursive(5) == 120

    with pytest.raises(ValueError):
        assert factorial(-5)

    with pytest.raises(ValueError):
        assert factorial_recursive(-5)

    with pytest.raises(TypeError):
        assert factorial('ewfewj')

    with pytest.raises(TypeError):
        assert factorial_recursive('ewfewj')
