class EmptyStack(Exception):
    def __init__(self):
        super().__init__('Стек пуст')


class EmptyQueue(Exception):
    def __init__(self):
        super().__init__('Очередь пуста')
