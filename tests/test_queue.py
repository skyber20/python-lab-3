import pytest
from src import Queue
from src.exceptions import EmptyQueue


def test_queue_methods():
    queue = Queue()

    assert queue.head is None
    assert (not queue.size) == queue.is_empty()

    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(11)

    assert queue.front() == 5
    assert queue.size == len(queue) == 3

    queue.dequeue()
    queue.dequeue()

    assert queue.front() == 11
    assert queue.size == len(queue) == 1

    queue = Queue([5, 10, 3, 7, 32])

    assert queue.front() == 5
    assert queue.size == len(queue) == 5


def test_queue_error():
    queue = Queue()

    assert not len(queue)

    with pytest.raises(EmptyQueue):
        assert queue.front()

    with pytest.raises(EmptyQueue):
        assert queue.dequeue()

