from src.structurs.node_stack import Node
from src.exceptions import EmptyStack


class Stack:
    def __init__(self, lst=None):
        self.head = None
        self.size = 0

        if lst is not None:
            for i in lst:
                self.push(i)

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            current_mn = data
        else:
            new_node.next = self.head
            current_mn = min(self.head.cur_mn, data)

        new_node.cur_mn = current_mn
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1

            return value
        raise EmptyStack()

    def peek(self):
        if self.size:
            return self.head.data
        raise EmptyStack()

    def is_empty(self) -> bool:
        return not self.size

    def min(self):
        if self.size:
            return self.head.cur_mn
        raise EmptyStack()

    def __len__(self):
        return self.size
