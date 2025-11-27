class EmptyStack(Exception):
    def __init__(self):
        super().__init__('Стек пуст')


class EmptyQueue(Exception):
    def __init__(self):
        super().__init__('Очередь пуста')


class KeyAndCmpAreBothUsed(Exception):
    def __init__(self):
        super().__init__('Нельзя использовать key и cmp одновременно')
