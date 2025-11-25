from src.structurs.node_queue import Node
from src.exceptions import EmptyQueue


class Queue:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        self.size = 0

        if lst is not None:
            for i in lst:
                self.enqueue(i)

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

        self.size += 1

    def dequeue(self):
        if not self.size:
            raise EmptyQueue()

        value = self.head.data
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        self.size -= 1
        return value

    def front(self):
        if not self.size:
            raise EmptyQueue()
        return self.head.data

    def is_empty(self):
        return not self.size

    def __len__(self):
        return self.size
