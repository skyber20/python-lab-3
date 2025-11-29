from typing import Optional
from constants import ALGORITHMS, STRUCTURS, MATH_FUNCS
from benchmarks.benchmark import timeit_once
from generators.genetators import rand_int_array
from structurs.stack import Stack
from structurs.queue import Queue
from src.exceptions import EmptyStack, EmptyQueue


class CLIState:
    def __init__(self):
        self.stack: Optional[Stack] = None
        self.queue: Optional[Queue] = None


class CommandHandler:
    def __init__(self, state: CLIState):
        self.state = state
        self.commands = self._build_commands()

    def _build_commands(self) -> dict[str, callable]:
        commands = {
            'help': self.help_cmd,
            'exit': self.exit_cmd,
            'gen': self.generate_array,
            'stack': self.stack_cmd,
            'queue': self.queue_cmd
        }

        for name in MATH_FUNCS.keys():
            commands[name] = self.fib_fact

        for name in ALGORITHMS.keys():
            commands[name] = self.sorts

        return commands

    def help_cmd(self, inp: list[str]) -> bool:
        print('Список поддерживаемых команд:')
        print('gen', *MATH_FUNCS.keys(), *ALGORITHMS.keys(), *STRUCTURS.keys(), sep='\n')
        return True

    def exit_cmd(self, inp: list[str]) -> bool:
        print('Пока')
        return False

    def parse_arr(self, arr: str) -> list[int]:
        cleaned = arr.strip('[] ')
        if not cleaned:
            return []
        return [int(i.strip()) for i in cleaned.split(',')]

    def generate_array(self, inp: list[str]) -> bool:
        if len(inp) != 4:
            print('Для генерации данных введите размер массива, нижнюю и верхнюю границы')
            return True

        try:
            n = int(inp[1])
            low = int(inp[2])
            high = int(inp[3])
            arr = rand_int_array(n, low, high)
            print(arr)
        except ValueError:
            print('Вводимые данные должны быть числами')

        return True

    def fib_fact(self, inp: list[str]) -> bool:
        if len(inp) < 2:
            print('Введите число')
            return True

        try:
            n = int(inp[1])
        except ValueError:
            print('Введите целое число')
            return True

        try:
            if '-t' in inp:
                res, time_val = timeit_once(MATH_FUNCS[inp[0]], n)
                print(res)
                print(f'Время выполнения: {time_val}')
            else:
                res = MATH_FUNCS[inp[0]](n)
                print(res)
        except ValueError as e:
            print(str(e))

        return True

    def sorts(self, inp: list[str]) -> bool:
        if len(inp) < 2:
            print('Для сортировки нужен массив')
            return True

        try:
            data = self.parse_arr(inp[1])
            if '-t' in inp:
                res, time_val = timeit_once(ALGORITHMS[inp[0]], data)
                print(res)
                print(f'Время выполнения: {time_val}')
            else:
                res = ALGORITHMS[inp[0]](data)
                print(res)
        except ValueError:
            print('Формат массива должен быть [1, 2, 3]')

        return True

    def stack_cmd(self, inp: list[str]) -> bool:
        if len(inp) == 1:
            self.state.stack = Stack()
            print('Стек создан')
            return True

        if inp[1].startswith('['):
            data = self.parse_arr(inp[1])
            self.state.stack = Stack(data)
            print('Стек создан')
            return True

        if self.state.stack is None:
            print('Сначала создайте Стек')
            return True

        if inp[1] == 'push':
            if len(inp) == 3:
                try:
                    n = int(inp[2])
                    self.state.stack.push(n)
                except ValueError:
                    print('Введите число, чтобы добавить его в стек')
            else:
                print('Введите число, чтобы добавить его в стек')

        elif inp[1] == 'pop':
            try:
                value = self.state.stack.pop()
                print(value)
            except EmptyStack:
                print('Стек пуст')

        elif inp[1] == 'peek':
            try:
                value = self.state.stack.peek()
                print(value)
            except EmptyStack as e:
                print(str(e))

        elif inp[1] == 'is_empty':
            print(self.state.stack.is_empty())

        elif inp[1] == 'len':
            print(len(self.state.stack))

        elif inp[1] == 'min':
            try:
                value = self.state.stack.min()
                print(value)
            except EmptyStack:
                print('Стек пуст')

        else:
            print('Неизвестная команда стека')

        return True

    def queue_cmd(self, inp: list[str]) -> bool:
        if len(inp) == 1:
            self.state.queue = Queue()
            print('Очередь создана')
            return True

        if inp[1].startswith('['):
            data = self.parse_arr(inp[1])
            self.state.queue = Queue(data)
            print('Очередь создана')
            return True

        if self.state.queue is None:
            print('Сначала создайте Очередь')
            return True

        if inp[1] == 'enqueue':
            if len(inp) == 3:
                try:
                    n = int(inp[2])
                    self.state.queue.enqueue(n)
                except ValueError:
                    print('Введите число, чтобы добавить его в очередь')
            else:
                print('Введите число, чтобы добавить его в очередь')

        elif inp[1] == 'dequeue':
            try:
                value = self.state.queue.dequeue()
                print(value)
            except EmptyQueue:
                print('Очередь пуста')

        elif inp[1] == 'front':
            try:
                value = self.state.queue.front()
                print(value)
            except EmptyQueue:
                print('Очередь пуста')

        elif inp[1] == 'is_empty':
            print(self.state.queue.is_empty())

        elif inp[1] == 'len':
            print(len(self.state.queue))

        else:
            print('Неизвестная команда очереди')

        return True

    def handle_command(self, command: list[str]) -> bool:
        cmd_handler = self.commands.get(command[0])
        if cmd_handler:
            return cmd_handler(command)
        else:
            print(f'Неизвестная команда {command[0]}')
            return True
