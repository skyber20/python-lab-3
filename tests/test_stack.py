import pytest
from src import Stack
from src.exceptions import EmptyStack


def test_stack_methods():
    stack = Stack()

    assert stack.head is None
    assert (not stack.size) == stack.is_empty()

    stack.push(5)
    stack.push(3)
    stack.push(11)

    assert stack.peek() == 11
    assert stack.size == len(stack) == 3
    assert stack.min() == 3

    stack.pop()
    stack.pop()

    assert stack.peek() == 5
    assert stack.size == len(stack) == 1
    assert stack.min() == 5

    stack = Stack([5, 10, 2, 5, 8, 3])

    assert stack.peek() == 3
    assert stack.size == len(stack) == 6
    assert stack.min() == 2


def test_stack_error():
    stack = Stack()

    assert not len(stack)

    with pytest.raises(EmptyStack):
        assert stack.peek()

    with pytest.raises(EmptyStack):
        assert stack.pop()

    with pytest.raises(EmptyStack):
        assert stack.min()
